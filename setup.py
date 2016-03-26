#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages


short_description = "An amateur slideshow generator"
html_dir = 'gmhp/templates'
css_dir = 'gmhp/templates/themes'

htmls = []
for html in os.listdir(html_dir):
    item = os.path.join(html_dir, html)
    if os.path.isfile(item):
        htmls.append(item)
css = [os.path.join(css_dir, f) for f in os.listdir(css_dir)]
data_path = os.path.expanduser('~/.gmhp')
data_pair = [(os.path.join(data_path, html_dir[5:]), htmls),
             (os.path.join(data_path, css_dir[5:]), css)]
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
