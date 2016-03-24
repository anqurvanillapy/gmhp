#!/usr/bin/env python
# -*- coding: utf-8 -*-

import markdown


class Generator(object):
    """Main part of the slideshow generator"""
    def __init__(self, arg):
        self.fn = arg.ifile
        self.theme = arg.theme

    def run(self):
        """Render template"""
        fn = self.fn
        css = self.load_theme(self.theme)

    def load_theme(self, theme):
        try:
            print(__file__)
        except AttributeError:
            raise "no such themes named %s" % theme
