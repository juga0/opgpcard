
Installation
=============

Installation for developers
-----------------------------

It is recommended to install ``opgpcard`` in a python virtual environment.

Check https://virtualenv.pypa.io/en/latest/installation.html. In Debian::

    sudo apt install python-virtualenv

Create a virtual environment::

    mkdir ~/.virtualenvs
    virtualenv ~/.virtualenvs/opgpcardenv
    source ~/.virtualenvs/opgpcardenv/bin/activate

Get the sources::

    git clone https://github.com/juga0/opgpcard

Install it::

    pip install -e .
