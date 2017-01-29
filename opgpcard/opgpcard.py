#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:ts=4:sw=4:expandtab 2

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

"""opgpcard main functions"""

import logging
import os
import os.path
import lxml.etree as etree

from .conf import (SVG_NAMESPACE, TEMPLATE_10_PATH, XPATH_CARD_SQUARE,
                   XPATH_QRCODE, CARD_10_NAME, XPATH_CARD_QRCODE,
                   TEMPLATE_PATH,
                   CARD_NAME, VCARD_NAME, QRCODE_NAME,
                   SVG_EXT, CARD_NAME_NO_QRCODE, CARD_10_NAME_NO_QRCODE)

from . import vcard_utils
from . import qrsvg
from . import gpg_utils

logger = logging.getLogger(__name__)
__all__ = ['fp_no_spaces', 'fp_spaces', 'extract_card_qr_coord',
           'gen_base_card_tree', 'include_qr_elem_path_in_card',
           'gen_opgpcard']


def fp_no_spaces(fp):
    fpnospaces = ''.join(fp.split())
    return fpnospaces


def fp_spaces(fp):
    fpnospaces = fp_no_spaces(fp)
    fpspaces = ' '.join([fpnospaces[i:i+4]
                         for i in range(0, len(fpnospaces), 4)])
    return fpspaces


def extract_card_qr_coord(xpath_square,
                          template_path=TEMPLATE_PATH):
    tree = etree.parse(template_path)
    elements = tree.xpath(xpath_square,
                          namespaces={'svg': SVG_NAMESPACE})
    if elements:
        e = elements[0]
        keys = ['x', 'y', 'height', 'width']
        attrs = {x: e.get(x) for x in keys}
        logger.debug('Card qr square attrs %s', attrs)
        return attrs
    return None


def gen_base_card_tree(xpath_text_dict, card_path,
                       template_path=TEMPLATE_PATH):
    tree = etree.parse(template_path)
    for xpath, text in list(xpath_text_dict.items()):
        elements = tree.xpath(xpath,
                              namespaces={'svg': SVG_NAMESPACE})
        if elements:
            elements[0].text = text
            logger.debug('Added text %s to card', text)
    tree.write(card_path)
    logger.info('Generated base card in %s', card_path)
    return tree


def include_qr_elem_path_in_card(card_path, card_tree, qr_svg_path):
    elements = card_tree.xpath(XPATH_CARD_QRCODE,
                               namespaces={'svg': SVG_NAMESPACE})
    if elements:
        logger.debug('Appending QRcode to the card.')
        e = elements[0]
        e.append(qr_svg_path)
    else:
        logger.warn('No elements found to apend the QRcode')
    card_tree.write(card_path)
    logger.debug('Card tree with QR: %s', etree.tostring(card_tree))
    logger.info('QR Code included in card %s', card_path)
    return card_tree


def gen_opgpcard(args):
    # parse args
    if args.mail and not args.fingerprint and not \
            args.firstname and not args.lastname:
        logger.debug('Obtaining attributes for key %s', args.mail)
        a = gpg_utils.obtain_key_attrs_from_email(args.mail)
        if a is not None:
            args.fingerprint = a['fingerprint']
            args.firstname = a['fname']
            args.lastname = a['lname']
    elif not args.mail and not args.fingerprint and not \
            args.firstname and not args.lastname:
        logger.debug('Obtaining keys')
        a = gpg_utils.obtain_key_attrs()
        if a is not None:
            args.mail = a['mail']
            args.fingerprint = a['fingerprint']
            args.firstname = a['fname']
            args.lastname = a['lname']
    # initialize file paths
    output_path = args.outputdir
    if not os.path.isdir(output_path):
        os.makedirs(output_path)
    # file paths
    vcard_path = os.path.join(output_path, VCARD_NAME %
                              (args.firstname + args.lastname,))
    qr_path = os.path.join(output_path, QRCODE_NAME %
                           (args.firstname + args.lastname,)) + SVG_EXT
    card_path_no_qrcode = os.path.join(output_path,
                                       CARD_NAME_NO_QRCODE %
                                       (args.firstname +
                                        args.lastname,))
    card_path = os.path.join(output_path, CARD_NAME %
                             (args.firstname + args.lastname,))

    card_10_path_no_qrcode = os.path.join(output_path,
                                          CARD_10_NAME_NO_QRCODE %
                                          (args.firstname +
                                           args.lastname,))
    card_10_path = os.path.join(output_path, CARD_10_NAME %
                                (args.firstname + args.lastname,))
    # generate vcard
    fpnospaces = fp_no_spaces(args.fingerprint)
    vcard_dict = vcard_utils.gen_vcard_attrs_dict(args.firstname,
                                                  args.lastname,
                                                  args.mail,
                                                  fpnospaces)
    vcard = vcard_utils.gen_vcard(vcard_dict, vcard_path)

    # generate card text
    fpspaces = fp_spaces(args.fingerprint)
    text_xpath = vcard_utils.gen_text_xpath_dict(args.firstname,
                                                 args.lastname,
                                                 args.mail,
                                                 fpspaces,
                                                 args.localsign)

    # card svg
    card_tree = gen_base_card_tree(text_xpath,
                                   card_path_no_qrcode,
                                   TEMPLATE_PATH)

    square_attrs = extract_card_qr_coord(XPATH_CARD_SQUARE,
                                         TEMPLATE_PATH)

    # qrcode svg
    qr_img, qr_img_box_width = qrsvg.gen_qr_svgimage(vcard, qr_path)
    qr_svg_path = qrsvg.extract_qr_elem_path(qr_path,
                                             XPATH_QRCODE)
    qr_svg_width = qrsvg.obtain_qr_svg_width(qr_path)
    qr_elem_path_transformed = qrsvg.add_transform_attr_qr_elem_path(
                                    square_attrs,
                                    qr_svg_path,
                                    qr_svg_width
                               )

    include_qr_elem_path_in_card(card_path, card_tree,
                                 qr_elem_path_transformed)
    # 10 DINA4
    card_10_tree = gen_base_card_tree(text_xpath,
                                      card_10_path_no_qrcode,
                                      TEMPLATE_10_PATH)

    include_qr_elem_path_in_card(card_10_path, card_10_tree,
                                 qr_elem_path_transformed)
