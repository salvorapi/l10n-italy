========================================
ITA - Fattura elettronica - Supporto PEC
========================================

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:4fe01cacb58719b623bdeec0c9809417bb991d5dde7049514dee9346a1311f67
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Fl10n--italy-lightgray.png?logo=github
    :target: https://github.com/OCA/l10n-italy/tree/16.0/l10n_it_fatturapa_pec
    :alt: OCA/l10n-italy
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/l10n-italy-16-0/l10n-italy-16-0-l10n_it_fatturapa_pec
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :target: https://runboat.odoo-community.org/builds?repo=OCA/l10n-italy&target_branch=16.0
    :alt: Try me on Runboat

|badge1| |badge2| |badge3| |badge4| |badge5|

**Italiano**

Questo modulo consente di inviare e ricevere i file XML della fattura
elettronica versione 1.2

http://www.fatturapa.gov.it/export/fatturazione/en/sdi.htm

via PEC.

Analizza le notifiche provenienti dallo SdI e monitora lo stato della
trasmissione.

**English**

This module allows you to send and receive electronic invoice/bill XML
files version 1.2

http://www.fatturapa.gov.it/export/fatturazione/en/sdi.htm

via PEC.

Notifications from ES are parsed and transmission state is tracked.

**Table of contents**

.. contents::
   :local:

Configuration
=============

**Italiano**

Consultare il modulo l10n_it_sdi_channel.

Creare un nuovo canale di tipo PEC (unico supportato per ora) e
indicare:

- Il server PEC da utilizzare per inviare/ricevere attraverso lo SdI
- La email PEC dello SdI, inizialmente uguale a sdi01@pec.fatturapa.it

Dopo il primo invio, lo SdI risponderà segnalando l'indirizzo da
utilizzare per gli invii successivi, da inserire nella configurazione
del server PEC dedicato.

Nella configurazione del server smtp, sezione "PEC e fattura
elettronica", selezionare la casella "Server PEC e-fattura".

Indicare quindi la email da usare per l'invio e la ricezione,
solitamente è uguale al nome utente di connessione (può essere diversa
in casi particolari).

È preferibile avere una email dedicata solo alla fatturazione
elettronica, in quanto i messaggi di altro tipo non possono essere
gestiti da Odoo (verrebbero marcati comunque come letti).

Se si usano altri server SMTP per l'invio di email non PEC, è necessario
aumentare la loro priorità rispetto a quella del server PEC.

Lo stato dell'esportazione XML può essere forzato impostando 'Permettere
di forzare lo stato dell'esportazione e-fattura' nelle impostazioni
tecniche dell'utente.

Per ogni azienda, in

Contabilità → Configurazione → Impostazioni → Fatture elettroniche

specificare l'utente che sarà utilizzato come creatore delle e-fatture
fornitore create dalla PEC.

**English**

See l10n_it_sdi_channel module.

Create a new PEC channel type (the only one supported right now) and
indicate:

- PEC server to be used for sending to/receiving from ES
- ES PEC email, initially equal to sdi01@pec.fatturapa.it

After sending the first email, ES will reply indicating the address to
use for all the others, to be entered in dedicated PEC server
configuration.

In smtp server configuration, select 'E-invoice PEC server' in 'PEC and
Electronic Invoice' section.

Then specify the email to use for sending and receiving, it is usually
equal to connection username (can be different in special cases).

It would be better to have a dedicated email for electronic invoicing,
because other kind of messages can't be managed by Odoo (they would be
marked as seen).

If you use other SMTP servers for non-PEC email sending, you need to
increase their priority as compared to PEC server one.

XML export state can ba forced setting 'Allow to force the supplier
e-bill export state' in user's technical settings.

For every company, in

Accounting → Configuration → Settings → Electronic Invoices

set the user who will be used as creator of supplier e-bill
automatically created from PEC.

Usage
=====

**Italiano**

Nell'allegato fattura elettronica in uscita fare clic sul pulsante
"Invia con PEC".

Le fatture elettroniche fornitore vengono create in modo automatico,
prelevate dalla casella PEC.

**English**

In electronic invoice out attachment you can click "Send Via PEC"
button.

Supplier electronic bills are automatically created, fetched from PEC
mailbox.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/l10n-italy/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/OCA/l10n-italy/issues/new?body=module:%20l10n_it_fatturapa_pec%0Aversion:%2016.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
-------

* Openforce Srls Unipersonale

Contributors
------------

- Andrea Colangelo <andreacolangelo@openforce.it>
- Sergio Corato <info@efatto.it>
- Lorenzo Battistini <https://github.com/eLBati>
- Sergio Zanchetta <https://github.com/primes2h>
- `Tecnativa <https://www.tecnativa.com>`__:

  - Víctor Martínez

- `Ooops <https://www.ooops404.com>`__:

  - Giovanni Serra <giovanni@gslab.it>

- Giuseppe Borruso <gborruso@dinamicheaziendali.it>

Maintainers
-----------

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the `OCA/l10n-italy <https://github.com/OCA/l10n-italy/tree/16.0/l10n_it_fatturapa_pec>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
