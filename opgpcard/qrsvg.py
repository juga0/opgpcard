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

"""opgpcard functions to generate QR code."""
import logging
import lxml.etree as etree
from qrcode.main import QRCode
from qrcode.image.svg import SvgPathImage

from . import conf

logger = logging.getLogger(__name__)
__all__ = ['gen_qr_svgimage', 'extract_qr_elem_path', 'obtain_qr_svg_width',
           'add_transform_attr_qr_elem_path']


def gen_qr_svgimage(vcard, qr_path):
    qr = QRCode(image_factory=SvgPathImage)
    qr.add_data(vcard)
    # img = qr.make_image(image_factory=SvgPathImage)
    img = qr.make_image(fit=True)
    # NOTE: img.get_image() will return a lxml svg element,
    # but without the qr path element.
    # Probably there is other way to obtain it other than having to save
    # the image
    # img.save(six.BytesIO())
    img.save(qr_path)
    logger.info('QRCode generated in %s, width: %s', qr_path, img.width)
    return img, img.width


def extract_qr_elem_path(qr_path, qr_svg_path_xpath):
    tree = etree.parse(qr_path)
    elements = tree.xpath(qr_svg_path_xpath,
                          namespaces={'svg': conf.SVG_NAMESPACE})
    if elements:
        e = elements[0]
        logger.debug('Extracted QR element path %s.', e)
        return e
    return None


def obtain_qr_svg_width(qr_path):
    tree = etree.parse(qr_path)
    root = tree.getroot()
    qr_svg_width = float(root.get('width').strip('mm'))
    logger.debug('QR Code element width %s', qr_svg_width)
    return qr_svg_width


def add_transform_attr_qr_elem_path(square_attrs, qr_svg_path,
                                    qr_svg_width):
    square_width = float(square_attrs['width'].strip('mm'))
    scale_factor = square_width/qr_svg_width
    # NOTE: if the element will be resized when it is already placed in the
    # card, it would be needed to calculate the new translate
    # coordinates, but as it has not been placed yet, the coordinates
    # are the same as for the square.
    # NOTE: the translate coordinates could be calculated as:
    # float(square_attrs['x']) - float(square_attrs['x']) * scale_factor
    qr_x = float(square_attrs['x'])
    qr_y = float(square_attrs['y'])
    transform_matrix = (scale_factor, 0, 0, scale_factor, qr_x, qr_y)
    qr_svg_path.set('transform', 'matrix%s' % str(transform_matrix))
    logger.debug('QRCode transform matrix %s', transform_matrix)
    return qr_svg_path
