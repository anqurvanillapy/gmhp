#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
import argparse
from gen import Generator


def init_path():
    """checkout whether in path"""
    path = os.getcwd()
    if path not in sys.path:
        sys.path.append(path)


def parse_arguments():
    """Parse CLI arguments, mainly importing Markdown files."""
    intro = 'An amateur slideshow generator.'
    parser = argparse.ArgumentParser(description=intro)
    parser.add_argument(
        'ifilename',
        action='store',
        metavar='inputname',
        nargs=1,
        help='specify your input Markdown filename')
    parser.add_argument(
        'ofilename',
        action='store',
        metavar='outputname',
        nargs=1,
        help='specify the output HTML format filename')
    parser.add_argument(
        '--theme', '-t',
        action='store',
        dest='theme',
        nargs=1,
        default=['white'],
        help='choose a theme')
    return parser.parse_args()


def main():
    init_path()
    args = parse_arguments()
    g = Generator(args)
    g.run()


if __name__ == '__main__':
    main()
