#!/usr/bin/env python

# Copyright (C) 2013 - 2014 SignalFx, Inc.
# Setuptools install description file.

from setuptools import setup, find_packages

from utils import __title__ as name, __version__ as version

with open('README.md') as readme:
    long_description = readme.read()

with open('requirements.txt') as f:
    requirements = [line.strip() for line in f.readlines()]

setup(
    name=name,
    version=version,
    description='Utility Scripts/Tools',
    long_description=long_description,
    zip_safe=True,
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'calculator='
                'utils.calculator:main',
            ],
    },
    url='http://github.com/ramjothikumar/utils',
)
