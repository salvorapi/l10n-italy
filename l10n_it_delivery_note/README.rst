============================
ITA - Documento di trasporto
============================

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:90eb24fd52ab8bebd1d8d50dcd8ae7c24be282de1b4ee6b966f6808726d6b31b
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Fl10n--italy-lightgray.png?logo=github
    :target: https://github.com/OCA/l10n-italy/tree/16.0/l10n_it_delivery_note
    :alt: OCA/l10n-italy
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/l10n-italy-16-0/l10n-italy-16-0-l10n_it_delivery_note
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :target: https://runboat.odoo-community.org/builds?repo=OCA/l10n-italy&target_branch=16.0
    :alt: Try me on Runboat

|badge1| |badge2| |badge3| |badge4| |badge5|

**English**

This module manage the Italian DDT (Delivery note).

From a picking is possible to generate a Delivery Note and group more
picking in one delivery note. It's also possible to invoice from the
delivery note form.

This module is alternative to ``l10n_it_ddt``, it follows the Odoo way
to process sale orders, pickings and invoices.

You can't have both ``l10n_it_ddt`` and ``l10n_it_delivery_note``
installed together.

There are two available settings:

- Base (default): one picking, one DN.
- Advanced: more picking in one DN.

**Italiano**

Questo modulo consente di gestire i DDT.

Da un prelievo è possibile generare un DDT e raggruppare più prelievi in
un DDT. È anche possibile fatturare dalla scheda del DDT.

Questo modulo è un alternativa al modulo ``l10n_it_ddt``, segue la
modalità Odoo di gestire ordini di vendita, prelievi e fatture.

Non è possibile avere installati contemporaneamente ``l10n_it_ddt`` e
``l10n_it_delivery_note``.

Ci sono due impostazioni possibili.

- Base (predefinita): un prelievo, un DDT.
- Avanzata: più prelievi in un DDT.

**Table of contents**

.. contents::
   :local:

Configuration
=============

To configure this module, go to:

1. *Inventory → Configuration → Settings - Delivery Notes*

   Checking 'Use Advanced DN Features' allows you to manage more picking
   on one delivery note.

   Checking 'Display Ref. Order in Delivery Note Report' or 'Display
   Ref. Customer in Delivery Note Report" enables in report fields
   relating DN line to SO (if applicable).

   Checking 'Display Carrier in Delivery Note Report' enables in report
   field 'Carrier'.

   Checking 'Display Delivery Method in Delivery Note Report' enables in
   report field 'Delivery Method'.

2. *Inventory → Configuration → Warehouse Management → Delivery Note
   Types*

   In delivery note type you can specify if the product price have to be
   printed in the delivery note report/slip.

   - *Inventory → Configuration → Delivery Notes → Conditions of
     Transport*
   - *Inventory → Configuration → Delivery Notes → Appearances of Goods*
   - *Inventory → Configuration → Delivery Notes → Reasons of Transport*
   - *Inventory → Configuration → Delivery Notes → Methods of Transport*

3. *Settings → User & Companies → Users*

   In the user profile settings, "Show product information in DN lines"
   allows showing prices in the form.

Usage
=====

Funzionalità base
-----------------

Quando un prelievo viene validato compare una scheda DDT.

Nella scheda fare clic su "Crea nuovo", si apre un procedura guidata
dove scegliere il tipo di DDT, quindi confermare. Immettere i dati
richiesti e poi fare clic su "Valida" per numerare il DDT.

Una volta validato, è possibile emettere fattura direttamente dal DDT se
il DDT stesso è di tipo consegna a cliente (In uscita) e si hanno i
permessi sull'utente.

È possibile annullare il DDT, reimpostarlo a bozza e poi modificarlo. Se
il DDT è fatturato il numero e la data non sono modificabili.

Per i trasferimenti tra magazzini creare un prelievo di tipo interno con
le relative ubicazioni. Validare il prelievo visualizza la scheda DDT.

È possibile anche avere DDT in ingresso, ovvero dopo la validazione del
prelievo selezionare la scheda per indicare il numero del DDT fornitore
e la data.

Funzionalità avanzata
---------------------

Vengono attivate varie funzionalità aggiuntive:

- più prelievi per un DDT
- selezione multipla di prelievi e generazione dei DDT
- aggiunta righe nota e righe sezione descrittive.
- lista dei DDT.

Il report DDT stampa in righe aggiuntive i lotti/seriali e le scadenze
del prodotto.

Il prezzo può essere indicato anche nel report DDT se nel tipo DDT è
indicata la stampa prezzi. La visibilità dei prezzi si trova nei
permessi dell'utente.

Le fatture generate dai DDT contengono i riferimenti al DDT stesso nelle
righe nota.

Accesso da portale
------------------

Gli utenti portal hanno la possibilità di scaricare i report dei DDT di
cui loro o la loro azienda padre sono impostati come destinatari o
indirizzo di spedizione.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/l10n-italy/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/OCA/l10n-italy/issues/new?body=module:%20l10n_it_delivery_note%0Aversion:%2016.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
-------

* Marco Calcagni
* Gianmarco Conte
* Link IT Europe Srl

Contributors
------------

- Riccardo Bellanova <r.bellanova@apuliasoftware.it>

- Matteo Bilotta <mbilotta@linkeurope.it>

- Giuseppe Borruso <gconte@dinamicheaziendali.it>

- Marco Calcagni <mcalcagni@dinamicheaziendali.it>

- Marco Colombo <marco.colombo@gmail.com>

- Gianmarco Conte <gconte@dinamicheaziendali.it>

- Letizia Freda <letizia.freda@netfarm.it>

- Andrea Piovesana <andrea.m.piovesana@gmail.com>

- Alex Comba <alex.comba@agilebg.com>

- `Ooops <https://www.ooops404.com>`__:

     - Giovanni Serra <giovanni@gslab.it>
     - Foresti Francesco <francesco.foresti@ooops404.com>

- Nextev Srl <odoo@nextev.it>

- `PyTech-SRL <https://www.pytech.it>`__:

     - Alessandro Uffreduzzi <alessandro.uffreduzzi@pytech.it>
     - Sebastiano Picchi <sebastiano.picchi@pytech.it>

- `Aion Tech <https://aiontech.company/>`__:

  - Simone Rubino <simone.rubino@aion-tech.it>

Maintainers
-----------

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

.. |maintainer-MarcoCalcagni| image:: https://github.com/MarcoCalcagni.png?size=40px
    :target: https://github.com/MarcoCalcagni
    :alt: MarcoCalcagni
.. |maintainer-aleuffre| image:: https://github.com/aleuffre.png?size=40px
    :target: https://github.com/aleuffre
    :alt: aleuffre
.. |maintainer-renda-dev| image:: https://github.com/renda-dev.png?size=40px
    :target: https://github.com/renda-dev
    :alt: renda-dev

Current `maintainers <https://odoo-community.org/page/maintainer-role>`__:

|maintainer-MarcoCalcagni| |maintainer-aleuffre| |maintainer-renda-dev| 

This module is part of the `OCA/l10n-italy <https://github.com/OCA/l10n-italy/tree/16.0/l10n_it_delivery_note>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
