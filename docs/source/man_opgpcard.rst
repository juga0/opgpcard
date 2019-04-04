OpenPGP printable card - opgpcard(1)
====================================

SYNOPSIS
--------

usage: opgpcard [-h] [-d] [-v] [-f FIRSTNAME] [-l LASTNAME] [-m MAIL]
                [-p FINGERPRINT] [-s] [-o OUTPUTDIR]

DESCRIPTION
------------

Create a VCard, a QR code and/or a printable business cards including
OpenPGP key and fingerprint.

OPTIONS
---------

If --fingerprint, --mail AND either --firstname or --lastname are provided,
a card is generated with those arguments.

If --fingerprint, --mail, --firstname OR --lastname are provided,
it will search for keys matching those arguments in that order,
and use the data from the first key and UID found.

If no arguments are provided, it will search for private keys and use the
data from the first key and UID found.

It will exit with error in any other case.

Optional arguments
~~~~~~~~~~~~~~~~~~

-h, --help
   Show help message and exit.

--version
   Show this program version and exit

--debug
   Set logging level to debug (default: False)

-f FIRSTNAME, --firstname FIRSTNAME

-l LASTNAME, --lastname LASTNAME

-m MAIL, --mail MAIL

-p FINGERPRINT, --fingerprint FINGERPRINT

-s, --localsign
   (default: True)

-o OUTPUTDIR, --outputdir OUTPUTDIR
   (default: output/)

BUGS
----

Please report bugs at https://github.com/juga0/opgpgcard.
