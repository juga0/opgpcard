opgpcard - OpenPGP Card
=======================

.. .. image:: https://badge.fury.io/py/opgpcard.svg
..     :target: https://badge.fury.io/py/opgpcard
..     :alt: Latest stable version
.. currently not working
.. .. image:: https://travis-ci.org/juga0/opgpcard.svg?branch=master
..     :target: https://travis-ci.org/juga0/opgpcard?branch=master
..     :alt: Travis-CI

Create a VCard, a QR code and/or a printable business cards including
OpenPGP key and fingerprint.

``opgpcard`` is a tool to create a VCard [0] including OpenPGP [1] key
and fingerprint, a QR code [2] of the VCard, a SVG [3] image formatted
as a "business" card [4] to print including the QR code and or a batch
of 10 those "business" cards to print in DIN4.

The idea comes from the Debian pgp-tools [5] ``gpg-key2ps`` script,
which *output a PostScript file which has your Key-ID, UIDs and
fingerprint nicely formatted for printing paper slips to take with you
to a signing-party.*

However the slips do not have the format of a standard "business" card
and they tend to be lost.

Sadly, most of the Address book [5] applications out there, do not
implement the VCard properties [6] for OpenPGP, so when the QR code in
these cards is scanned, the Address book application will import the
mail address, but probably will ignore the OpenPGP key and/or
fingerprint.

[0] https://en.wikipedia.org/wiki/VCard

[1] https://en.wikipedia.org/wiki/QR_code

[2] https://en.wikipedia.org/wiki/Pretty_Good_Privacy#OpenPGP

[3] https://en.wikipedia.org/wiki/SVG

[5] https://pgp-tools.alioth.debian.org/

[4] https://en.wikipedia.org/wiki/Business_card

[5] https://en.wikipedia.org/wiki/Address_book#Software_address_book

[6] https://en.wikipedia.org/wiki/VCard#Properties

Installation
------------

See `<docs/source/install.rst>`_ (in the local directory or GitHub) or
`<https://opgpcard.readthedocs.io/en/latest/install.html>`_ .

Download
--------

You can download this project in either
`zip <http://github.com/juga0/opgpcard/zipball/master>`__ or
`tar <http://github.com/juga0/opgpcard/tarball/master>`__ formats.

You can also clone the project with Git by running::

    git clone https://github.com/juga0/opgpcard

Bugs and features
-----------------

To report a bug or a feature request, please fill in an issue on the
`opgpcard issue tracker <https://github.com/juga0/opgpcard/issues>`__.

License
-------

``opgpcard`` is Copyright 2016, 2017, 2018 by juga (juga at riseup dot net)
under the terms of the `GPLv3 <http://www.gnu.org/licenses/>`__ license.
