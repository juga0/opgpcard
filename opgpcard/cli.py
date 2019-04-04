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

"""opgpcard main script."""

import argparse
import logging

from . import __version__
from .conf import OUTPUT_DIR
from .opgpcard import gen_opgpcard


def create_args_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d',
                        '--debug',
                        help='Set logging level to debug',
                        action='store_true')
    parser.add_argument('-o', '--outputdir', help='',
                        default=OUTPUT_DIR)
    parser.add_argument('-v', '--version', action='version',
                        help='version',
                        version='%(prog)s ' + __version__)
    # Allow cards without any name
    parser.add_argument('-f', '--firstname', help='', default='')
    parser.add_argument('-l', '--lastname', help='', default='')
    parser.add_argument('-p', '--fingerprint', help='')
    parser.add_argument('-s', '--localsign', help='',
                        action='store_true', default=True)
    parser.add_argument('-m', '--mail', help='')
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
