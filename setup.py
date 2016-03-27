#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages


short_description = "An amateur slideshow generator"
html_dir = 'gmhp/templates'
themes_dir = 'gmhp/templates/themes'
fonts_dir = 'gmhp/templates/themes/fonts'

themes, htmls = [], []
for html in os.listdir(html_dir):
    item = os.path.join(html_dir, html)
    if os.path.isfile(item):
        htmls.append(item)
for theme in os.listdir(themes_dir):
    item = os.path.join(themes_dir, theme)
    if os.path.isfile(item):
        themes.append(item)
fonts = [os.path.join(fonts_dir, f) for f in os.listdir(fonts_dir)]
data_path = os.path.expanduser('~/.gmhp')
data_pair = [(os.path.join(data_path, html_dir[5:]), htmls),
             (os.path.join(data_path, themes_dir[5:]), themes),
             (os.path.join(data_path, fonts_dir[5:]), fonts)]
# print(data_pair)

try:
    long_description = open("README.md").read()
except IOError:
    long_description = short_description

setup(
    name="gmhp",
    version="0.1.0",
    description=short_description,
    license="MIT",
    author="AnqurVanillapy",
    author_email="anqurvanillapy@gmail.com",
    packages=find_packages(),
    data_files=data_pair,
    long_description=long_description,
    entry_points={
        'console_scripts': [
            'gmhp=gmhp:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ]
)
