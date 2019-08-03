
Installation
=============

The recommended method  is to install it from your system
distribution.

In Debian/Ubuntu systems::

    sudo apt install opgpcard

Installation for developers
---------------------------

System requirements
~~~~~~~~~~~~~~~~~~~

- Python 3 (>= 3.5)
- GPGME_
- SWIG_ (to build GPGME_)
- virtualenv_ (it is recommended to install the required python dependencies
  in a virtualenv)

In Debian::

    sudo apt install python3 swig libgpgme-dev virtualenv

Python dependencies
~~~~~~~~~~~~~~~~~~~

- qrcode_
- lxml_
- gpg_

To install the Python dependencies, create a ``virtualenv`` first

::

    virtualenv venv -p /usr/bin/python3
    source venv/bin/activate

Clone ``opgpcard``::

    git clone https://github.com/juga0/opgpcard.git

Install the python dependencies::

    cd opgpcard && pip install .

.. _SWIG: http://swig.org/
.. _GPGME: https://www.gnupg.org/related_software/gpgme/
.. _virtualenv: https://virtualenv.pypa.io/en/stable/installation/
.. _qrcode: https://pypi.python.org/pypi/qrcode/
.. _lxml: https://lxml.de/
.. _gpg: https://pypi.org/project/gpg/
