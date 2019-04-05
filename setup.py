#!/usr/bin/env python

#   This file is part of opgpcard, a set of scripts to
#   use different tor guards depending on the network we connect to.
#
#   Copyright (C) 2016-2019 juga (juga at riseup dot net)
#
#   opgpcard is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License Version 3 of the
#   License, or (at your option) any later version.
#
#   opgpcard is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with opgpcard.  If not, see <http://www.gnu.org/licenses/>.
#

from setuptools import setup, find_packages
import opgpcard

setup(
    name='opgpcard',
    version=opgpcard.__version__,
    description=opgpcard.__description__,
    long_description=opgpcard.__long_description__,
    author=opgpcard.__author__,
    author_email=opgpcard.__author_mail__,
    platforms=['unix', 'linux', 'osx', 'cygwin', 'win32'],
    license='GPLv3+',
    url=opgpcard.__website__,
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=["qrcode", "lxml", "gpg"],
    extras_require={
        # vulture: find unused code
        'dev': ['flake8', 'vulture'],
        'test': ['tox', 'pytest', 'coverage'],
        'doc': ['sphinx', 'pylint']
    },
    tests_require=['pytest'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'opgpcard = opgpcard.cli:main',
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        "Environment :: Console",
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 ' +
        'or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='python openpgp gpp businesscard vcard qrcode',
)
