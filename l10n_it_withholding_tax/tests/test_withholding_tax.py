# Copyright 2018 Lorenzo Battistini (https://github.com/eLBati)
# Copyright 2024 Simone Rubino - Aion Tech
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import time
from datetime import date, timedelta

from odoo import fields
from odoo.exceptions import ValidationError
from odoo.fields import first
from odoo.tests.common import Form, TransactionCase


class TestWithholdingTax(TransactionCase):
    def setUp(self):
        super().setUp()

        # Accounts
        self.wt_account_payable = self.env["account.account"].create(
            {
                "name": "Debiti per ritenute da versare",
                "code": "WT.001",
                "account_type": "liability_payable",
                "reconcile": True,
            }
        )
        self.wt_account_receivable = self.env["account.account"].create(
            {
                "name": "Crediti per ritenute subite",
                "code": "WT.002",
                "account_type": "asset_receivable",
                "reconcile": True,
            }
        )

        # Journals
        self.journal_misc = self.env["account.journal"].search(
            [("type", "=", "general")], limit=1
        )
        self.journal_bank = self.env["account.journal"].create(
            {"name": "Bank", "type": "bank", "code": "BNK67"}
        )

        # Payment Register
        self.payment_register_model = self.env["account.payment.register"]
        self.register_view_id = "account.view_account_payment_register_form"

        # Payments
        vals_payment = {
            "name": "",
            "line_ids": [(0, 0, {"value": "balance", "days": 15})],
        }
        self.payment_term_15 = self.env["account.payment.term"].create(vals_payment)

        # Withholding tax
        wt_vals = {
            "name": "Code 1040",
            "code": "1040",
            "certification": True,
            "account_receivable_id": self.wt_account_receivable.id,
            "account_payable_id": self.wt_account_payable.id,
            "journal_id": self.journal_misc.id,
            "payment_term": self.payment_term_15.id,
            "rate_ids": [
                (
                    0,
                    0,
                    {
                        "tax": 20,
                        "base": 1,
                    },
                )
            ],
        }
        self.wt1040 = self.env["withholding.tax"].create(wt_vals)

        # Supplier Invoice with WT
        invoice_line_vals = [
            (
                0,
                0,
                {
                    "quantity": 1.0,
                    "account_id": self.env["account.account"]
                    .search(
                        [("account_type", "=", "expense")],
                        limit=1,
                    )
                    .id,
                    "name": "Advice",
                    "price_unit": 1000.00,
                    "invoice_line_tax_wt_ids": [(6, 0, [self.wt1040.id])],
                    "tax_ids": False,
                },
            )
        ]
        self.invoice = self.env["account.move"].create(
            {
                "invoice_date": time.strftime("%Y") + "-07-15",
                "name": "Test Supplier Invoice WT",
                "journal_id": self.env["account.journal"]
                .search([("type", "=", "purchase")])[0]
                .id,
                "partner_id": self.env.ref("base.res_partner_12").id,
                "invoice_line_ids": invoice_line_vals,
                "move_type": "in_invoice",
            }
        )
        self.invoice._onchange_invoice_line_wt_ids()
        self.invoice.action_post()

    def test_withholding_tax(self):
        domain = [("name", "=", "Code 1040")]
        wts = self.env["withholding.tax"].search(domain)
        self.assertEqual(len(wts), 1, msg="Withholding tax was not created")

        self.assertEqual(
            self.invoice.withholding_tax_amount, 200, msg="Invoice WT amount"
        )
        self.assertEqual(
            self.invoice.amount_net_pay, 800, msg="Invoice WT amount net pay"
        )

        domain = [
            ("invoice_id", "=", self.invoice.id),
            ("withholding_tax_id", "=", self.wt1040.id),
        ]
        wt_statement = self.env["withholding.tax.statement"].search(domain)
        self.assertEqual(len(wt_statement), 1, msg="WT statement was not created")
        self.assertEqual(wt_statement.base, 1000, msg="WT statement Base amount")
        self.assertEqual(wt_statement.amount, 0, msg="WT statement amount applied")
        self.assertEqual(wt_statement.amount_paid, 0, msg="WT statement Base paid")

        self.assertEqual(self.invoice.amount_net_pay, 800)
        self.assertEqual(self.invoice.amount_net_pay_residual, 800)

        ctx = {
            "active_model": "account.move",
            "active_ids": [self.invoice.id],
        }
        register_payments = self.payment_register_model.with_context(**ctx).create(
            {
                "payment_date": time.strftime("%Y") + "-07-15",
                "amount": 800,
                "journal_id": self.journal_bank.id,
                "payment_method_line_id": (
                    self.journal_bank.outbound_payment_method_line_ids[0].id
                ),
            }
        )
        register_payments.action_create_payments()

        partials = self.invoice._get_reconciled_invoices_partials()[0]

        # WT payment generation
        self.assertEqual(len(partials), 2, msg="Missing WT payment")

        # WT amount in payment move lines
        self.assertTrue({p[1] for p in partials} == {800, 200})

        # WT amount applied in statement
        domain = [
            ("invoice_id", "=", self.invoice.id),
            ("withholding_tax_id", "=", self.wt1040.id),
        ]
        wt_statement = self.env["withholding.tax.statement"].search(domain)
        self.assertEqual(wt_statement.amount, 200)
        self.assertEqual(self.invoice.state, "posted")
        self.assertEqual(self.invoice.amount_net_pay, 800)
        self.assertEqual(self.invoice.amount_net_pay_residual, 0)

    def test_partial_payment(self):
        self.assertEqual(self.invoice.amount_net_pay, 800)
        self.assertEqual(self.invoice.amount_net_pay_residual, 800)
        ctx = {
            "active_model": "account.move",
            "active_ids": [self.invoice.id],
            "active_id": self.invoice.id,
            "default_reconciled_invoice_ids": [(4, self.invoice.id, None)],
        }
        register_payments = self.payment_register_model.with_context(**ctx).create(
            {
                "payment_date": time.strftime("%Y") + "-07-15",
                "amount": 600,
                "journal_id": self.journal_bank.id,
                "payment_method_line_id": (
                    self.journal_bank.outbound_payment_method_line_ids[0].id
                ),
            }
        )
        register_payments.action_create_payments()

        partials = self.invoice._get_reconciled_invoices_partials()[0]

        # WT payment generation
        self.assertEqual(len(partials), 2, msg="Missing WT payment")

        # WT amount in payment move lines
        self.assertTrue({p[1] for p in partials} == {600, 150})

        # WT amount applied in statement
        domain = [
            ("invoice_id", "=", self.invoice.id),
            ("withholding_tax_id", "=", self.wt1040.id),
        ]
        wt_statement = self.env["withholding.tax.statement"].search(domain)
        self.assertEqual(wt_statement.amount, 150)
        self.assertEqual(self.invoice.amount_net_pay, 800)
        self.assertEqual(self.invoice.amount_net_pay_residual, 200)
        self.assertEqual(self.invoice.amount_residual, 250)
        self.assertEqual(self.invoice.state, "posted")

    def test_overlapping_rates(self):
        """Check that overlapping rates cannot be created"""
        with self.assertRaises(ValidationError):
            self.wt1040.rate_ids = [
                (
                    0,
                    0,
                    {
                        "date_start": fields.Date.to_string(
                            date.today() - timedelta(days=1)
                        )
                    },
                )
            ]

    def test_keep_selected_wt(self):
        """Check that selected Withholding tax is kept in lines."""
        invoice_line_vals = [
            (
                0,
                0,
                {
                    "quantity": 1.0,
                    "account_id": self.env["account.account"]
                    .search(
                        [("account_type", "=", "expense")],
                        limit=1,
                    )
                    .id,
                    "name": "Advice",
                    "price_unit": 1000.00,
                    "tax_ids": False,
                },
            )
        ]
        invoice = self.env["account.move"].create(
            {
                "invoice_date": time.strftime("%Y") + "-07-15",
                "name": "Test Supplier Invoice WT",
                "journal_id": self.env["account.journal"]
                .search([("type", "=", "purchase")])[0]
                .id,
                "partner_id": self.env.ref("base.res_partner_12").id,
                "invoice_line_ids": invoice_line_vals,
                "move_type": "in_invoice",
            }
        )
        invoice_form = Form(invoice)
        with invoice_form.invoice_line_ids.edit(0) as line_form:
            line_form.invoice_line_tax_wt_ids.clear()
            line_form.invoice_line_tax_wt_ids.add(self.wt1040)
        invoice = invoice_form.save()
        self.assertTrue(invoice.invoice_line_ids.invoice_line_tax_wt_ids)

    def test_duplicating_wt(self):
        new_tax = self.wt1040.copy()
        self.assertEqual(new_tax.code, "1040 (copy)")
        self.assertEqual(new_tax.name, "Code 1040")

    def test_create_payments(self):
        """Test create payment when Register Payment wizard
        is open from Bill tree view"""
        ctx = {
            "active_ids": [self.invoice.id],
            "active_model": "account.move",
        }
        f = Form(
            self.payment_register_model.with_context(**ctx), view=self.register_view_id
        )
        payment_register = f.save()
        # passing default_move_type="in_invoice" in the context in order
        # to simulate opening of payment_register from Bills tree view
        payment_register.with_context(
            default_move_type="in_invoice"
        ).action_create_payments()

    def test_wt_after_repost(self):
        wt_statement_ids = self.env["withholding.tax.statement"].search(
            [
                ("invoice_id", "=", self.invoice.id),
                ("withholding_tax_id", "=", self.wt1040.id),
            ]
        )
        self.assertEqual(len(wt_statement_ids), 1)
        ctx = {
            "active_model": "account.move",
            "active_ids": [self.invoice.id],
            "active_id": self.invoice.id,
            "default_reconciled_invoice_ids": [(4, self.invoice.id, None)],
        }
        register_payment_form = Form(
            self.payment_register_model.with_context(**ctx), view=self.register_view_id
        )
        register_payment_form.amount = 600
        register_payment = register_payment_form.save()
        register_payment.action_create_payments()
        partials = self.invoice._get_reconciled_invoices_partials()[0]
        self.assertTrue({p[1] for p in partials} == {600, 150})

        self.invoice.button_draft()
        self.invoice.action_post()
        wt_statement_ids = self.env["withholding.tax.statement"].search(
            [
                ("invoice_id", "=", self.invoice.id),
                ("withholding_tax_id", "=", self.wt1040.id),
            ]
        )
        self.assertEqual(len(wt_statement_ids), 1)
        debit_line_id = partials[0][2].move_id.line_ids.filtered(
            lambda line: line.debit
        )
        self.invoice.js_assign_outstanding_line(debit_line_id.id)
        self.assertEqual(self.invoice.amount_net_pay, 800)
        self.assertEqual(self.invoice.amount_net_pay_residual, 200)
        self.assertEqual(self.invoice.amount_residual, 250)
        self.assertEqual(self.invoice.state, "posted")

    def _get_payment_wizard(self, invoice):
        wizard_action = invoice.action_register_payment()
        wizard_model = wizard_action["res_model"]
        wizard_context = wizard_action["context"]
        wizard = self.env[wizard_model].with_context(**wizard_context).create({})
        return wizard

    def test_payment_reset_net_pay_residual(self):
        """The amount to pay is reset to the Residual Net To Pay
        when amount and Journal are changed."""
        # Arrange: Pay an invoice
        invoice = self.invoice
        wizard = self._get_payment_wizard(invoice)
        user_set_amount = 20
        # pre-condition
        self.assertEqual(
            wizard.amount,
            invoice.amount_net_pay_residual,
        )
        self.assertTrue(
            invoice.withholding_tax_amount,
        )

        # Act: Change amount
        wizard.amount = user_set_amount

        # Assert: User's change is kept
        self.assertEqual(
            wizard.amount,
            user_set_amount,
        )

        # Act: Change Journal
        wizard.journal_id = self.journal_bank

        # Assert: Amount is reset to the Residual Net To Pay
        self.assertEqual(
            wizard.amount,
            invoice.amount_net_pay_residual,
        )

    def test_wt_display_name(self):
        """The display name of statements and moves
        includes the partner and the tax."""
        # Arrange
        invoice = self.invoice
        partner = invoice.partner_id
        wt_tax = self.wt1040
        payment_wizard = self._get_payment_wizard(invoice)
        payment_wizard.action_create_payments()

        wt_statement = self.env["withholding.tax.statement"].search(
            [
                ("invoice_id", "=", invoice.id),
                ("withholding_tax_id", "=", wt_tax.id),
            ],
            limit=1,
        )
        wt_move = first(wt_statement.move_ids)
        # pre-condition
        self.assertTrue(wt_statement)
        self.assertTrue(wt_move)

        # Act
        wt_statement_display_name = wt_statement.display_name
        wt_move_display_name = wt_move.display_name

        # Assert
        self.assertIn(partner.name, wt_statement_display_name)
        self.assertIn(wt_tax.name, wt_statement_display_name)
        self.assertIn(partner.name, wt_move_display_name)
        self.assertIn(wt_tax.name, wt_move_display_name)
