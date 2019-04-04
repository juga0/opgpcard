# vim:ts=4:sw=4:expandtab 2

# Copyright 2016-2019 juga <juga@riseup.net>

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
"""opgpcard GPG utils"""

import logging
import gpg

logger = logging.getLogger(__name__)
__all__ = ['obtain_key_attrs_from_key', 'obtain_skeys',
           'obtain_key_from_email', 'obtain_key_attrs_from_email']


def obtain_key_attrs_from_key(key):
    # TODO: select which UIDs to include
    # TODO: obtain public key data
    name = key.uids[0].name
    email = key.uids[0].email
    if not name:
        name = email.split('@')[0]
    namesplitted = name.split()
    fname, lname = namesplitted[0], ' '.join(namesplitted[1:])
    fp = key.fpr
    key_attrs = {'mail': email, 'fingerprint': fp,
                 'fname': fname, 'lname': lname}
    logger.info('Using attributes from the first UID %s.', key_attrs)
    return key_attrs


def obtain_skeys():
    c = gpg.Context()
    skeys = list(c.keylist(secret=True))
    if skeys:
        logger.info('Found private keys in your keyring.')
    return skeys


def obtain_key_from_email(attr):
    # TODO: select key if there're several for the same email.
    c = gpg.Context()
    keys = list(c.keylist(attr))
    if not keys:
        return None
    logger.info('Using the first key found matching %s.', attr)
    key = keys[0]
    return key


def obtain_key_attrs_from_email(attr):
    key = obtain_key_from_email(attr)
    if key:
        attrs = obtain_key_attrs_from_key(key)
        return attrs
    return None


def obtain_key_attrs():
    skeys = obtain_skeys()
    if skeys:
        logger.info("Using the first key found.")
        attrs = obtain_key_attrs_from_key(skeys[0])
        return attrs
    return None
