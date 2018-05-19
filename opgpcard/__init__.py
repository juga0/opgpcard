# -*- coding: utf-8 -*-
# vim:ts=4:sw=4:expandtab

# Copyright 2016 juga <juga@riseup.net>

# This file is part of opgpcard.
#
# opgpcard is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# opgpcard is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with opgpcard.  If not, see <http://www.gnu.org/licenses/>.

try:
    from _version import version
except ImportError:
    try:
        from setuptools_scm import get_version
        version = get_version()
    except (ImportError, LookupError):
        version = '0.1.3'

__version__ = version
__author__ = "juga"
__author_mail__ = "juga@riseup.net"
__description__ = "Create a VCard, a QR code and/or a printable " \
                  "business cards including OpenPGP key and fingerprint."
__long_description__ = """opgpcard is a tool to create a VCard
including OpenPGP key and fingerprint, a QR code of the VCard,
a SVG image formatted as a business card to print including the QR code
and or a batch of 10 those business cards to print in DIN4."""
__website__ = 'https://github.com/juga0/opgpcard'
__documentation__ = 'http://opgpcard.readthedocs.io/en/' + __version__
__copyright__ = """Copyright (C) 2016, 2017, 2018 <juga@riseup.net>
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.
For details see the COPYRIGHT file distributed along this program."""
__license__ = """
This package is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
any later version.

This package is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this package. If not, see <http://www.gnu.org/licenses/>.
"""
