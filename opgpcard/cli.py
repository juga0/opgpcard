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

"""Create a VCard, a QR code and/or a printable business cards including
OpenPGP key and fingerprint.

If --fingerprint, --mail AND either --firstname or --lastname are provided,
a card is generated with those arguments.

If --fingerprint, --mail, --firstname OR --lastname are provided,
it will search for keys matching those arguments in that order,
and use the data from the first key and UID found.

If no arguments are provided, it will search for private keys and use the
data from the first key and UID found.

It will exit with error in any other case.
"""

import argparse
import logging

from . import __version__
from .conf import OUTPUT_DIR
from .opgpcard import gen_opgpcard


class RawTextArgumentDefaultsHelpFormatter(
        argparse.RawTextHelpFormatter, argparse.ArgumentDefaultsHelpFormatter
        ):
    pass


def create_args_parser():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=RawTextArgumentDefaultsHelpFormatter
        )
    parser.add_argument('-d',
                        '--debug',
                        help='Set logging level to debug',
                        action='store_true')
    parser.add_argument('-v', '--version', action='version',
                        help='Show this program version and exit',
                        version='%(prog)s ' + __version__)
    parser.add_argument('-f', '--firstname', default='')
    parser.add_argument('-l', '--lastname', default='')
    parser.add_argument('-m', '--mail')
    parser.add_argument('-p', '--fingerprint')
    parser.add_argument('-s', '--localsign', action='store_true', default=True)
    parser.add_argument('-o', '--outputdir', default=OUTPUT_DIR)
    return parser


def main():
    parser = create_args_parser()
    args = parser.parse_args()

    if args.debug:
        FORMAT = "%(levelname)s: %(filename)s:%(lineno)s -"\
                 "%(funcName)s - %(message)s"
        logging.basicConfig(format=FORMAT, level=logging.DEBUG)
        logger = logging.getLogger(__name__)
    else:
        from logging import handlers
        FORMAT = "%(asctime)s %(name)s %(module)s[%(process)s]:"\
                 " %(levelname)s - %(message)s"
        datefmt = "%b %d %H:%M:%S"
        logging.basicConfig(format=FORMAT, level=logging.INFO,
                            datefmt=datefmt)
        logger = logging.getLogger(__name__)
        h = handlers.SysLogHandler(address='/dev/log')
        formatter = logging.Formatter(FORMAT)
        h.setFormatter = formatter
        logger.addHandler(h)
    logger.debug('args %s', args)
    gen_opgpcard(args)


if __name__ == '__main__':
    main()
