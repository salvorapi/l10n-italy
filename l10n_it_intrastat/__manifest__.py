# Copyright 2019 Simone Rubino - Agile Business Group
# Copyright 2015 Camilli Alessandro - www.openforce.it
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "ITA - Intrastat",
    "version": "16.0.1.2.0",
    "category": "Account",
    "summary": "Riclassificazione merci e servizi per dichiarazioni Intrastat",
    "author": "Openforce, Link IT srl, Agile Business Group, "
    "Powerp network, "
    "Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/l10n-italy",
    "license": "AGPL-3",
    "depends": [
        "product",
        "stock",
        "stock_account",
        "uom",
    ],
    "data": [
        "security/intrastat_rules.xml",
        "security/ir.model.access.csv",
        "security/rules.xml",
        "data/account.intrastat.transaction.nature.csv",
        "data/account.intrastat.transaction.nature.b.csv",
        "data/account.intrastat.transport.csv",
        "data/account.intrastat.custom.csv",
        "data/report.intrastat.code.csv",
        "views/intrastat.xml",
        "views/product.xml",
        "views/account.xml",
        "views/config.xml",
    ],
    "demo": ["demo/product_demo.xml"],
}
