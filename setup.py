#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from datarum import __version__

setup(
    name='datarum',
    version=__version__,
    author='Mika Naylor (Autophagy)',
    author_email='mail@autophagy.io',
    url='https://github.com/Autophagy/datarum',
    description=('Datárum is a small python library to convert Gregorian '
                 'dates to Wending, an Old English variant on the French '
                 'Republican calendar, for use in various projects.'),
    long_description=open('README.rst', encoding='utf-8').read(),
    packages=['datarum'],
    python_requires='>=3',
    install_requires=['parse'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
)
