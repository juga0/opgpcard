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

"""opgpcard configuration."""
import os.path


SVG_NAMESPACE = "http://www.w3.org/2000/svg"
XPATH_FP = "//svg:tspan[@id='openpgp_fp']"
XPATH_LSIGN = "//svg:tspan[@id='only_lsign_text']"
XPATH_MAIL = "//svg:tspan[@id='mail_address']"
XPATH_FNAME = "//svg:tspan[@id='firstname']"
XPATH_LNAME = "//svg:tspan[@id='lastname']"
XPATH_QRCODE = "//svg:path[@id='qr-path']"
XPATH_CARD_QRCODE = "//svg:g[@id='QRcode']"
XPATH_CARD_SQUARE = "//svg:rect[@id='rect13153']"

DATA_DIR = 'data'
TEMPLATE_FILE = 'opgpcard_template.svg'
VCARD_TEMPLATE_FILE = 'opgpcard_template.vcf'
OUTPUT_DIR = 'output'
CARD_NAME = 'opgpcard_%s.svg'
CARD_NAME_NO_QRCODE = 'opgpcard_noqr_%s.svg'
VCARD_NAME = 'opgpcard_%s.vcf'
QRCODE_NAME = 'opgpcard_qr_%s'
QRCODE_NAME_RESIZED = 'opgpcard_qr_resized_%s'
SVG_EXT = '.svg'


TEMPLATE_10_FILE = 'opgpcard_template_DIN4_10.svg'
CARD_10_NAME = 'opgpcard_%s_DIN4_10.svg'
CARD_10_NAME_NO_QRCODE = 'opgpcard_noqr_%s_DIN4_10.svg'

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
ROOT_PATH, _ = os.path.split(os.path.realpath(BASE_PATH))
OUTPUT_PATH = os.path.join(ROOT_PATH, OUTPUT_DIR)
TEMPLATE_PATH = os.path.join(BASE_PATH, DATA_DIR, TEMPLATE_FILE)
VCARD_TEMPLATE_PATH = os.path.join(BASE_PATH, DATA_DIR, VCARD_TEMPLATE_FILE)
TEMPLATE_10_PATH = os.path.join(BASE_PATH, DATA_DIR, TEMPLATE_10_FILE)
