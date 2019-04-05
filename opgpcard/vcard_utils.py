# -*- coding: utf-8 -*-
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

"""opgpcard functions to generate VCard"""
import logging
import io

from . import conf

logger = logging.getLogger(__name__)
__all__ = ['gen_vcard_attrs_dict', 'gen_text_xpath_dict', 'gen_vcard']


def gen_vcard_attrs_dict(fname, lname, mail, fp):
    vcard_dict = {'fname': fname, 'lname': lname, 'mail': mail, 'fp': fp}
    logger.debug('vcard_dict %s.', vcard_dict)
    return vcard_dict


def gen_text_xpath_dict(fname, lname, mail, fp, lsign=True):
    if lsign:
        lsign_text = '(only local sign)'
    else:
        lsign_text = ''
    xpath_text_dict = {conf.XPATH_FNAME: fname,
                       conf.XPATH_LNAME: lname,
                       conf.XPATH_MAIL: mail,
                       conf.XPATH_FP: fp,
                       conf.XPATH_LSIGN: lsign_text}
    logger.debug('xpath_text_dict %s.', xpath_text_dict)
    return xpath_text_dict


def gen_vcard(vcard_dict, vcard_path,
              vcard_template_path=conf.VCARD_TEMPLATE_PATH):
    with io.open(vcard_template_path) as fp:
        vcard = fp.read()
    logger.debug('vcard template %s', vcard)
    vcard = vcard % vcard_dict
    logger.debug('vcard %s', vcard)
    with io.open(vcard_path, 'w') as fp:
        fp.write(vcard)
    logger.info('VCard generated in %s.', vcard_path)
    return vcard
