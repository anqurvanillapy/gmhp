#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
import base64
from markdown import markdown
from jinja2 import *
from pygments.formatters import HtmlFormatter


class Generator(object):
    """Main part of the slideshow generator"""
    def __init__(self, arg):
        self.ifn = arg.ifilename[0]
        self.ofn = arg.ofilename[0]
        self.theme = arg.theme[0]
        self.tmplpath = os.path.expanduser('~/.gmhp/templates')
        if not os.path.isdir(self.tmplpath):
            raise IOError("no template folder '.gmhp/templates' found"
                "in user path, please checkout your installlation")
        self.mdexts =  ['.markdown', '.mdown', '.mkdn', '.md', '.mkd',
                        '.mdwn', '.mdtxt', '.mdtext', '.text']

    def run(self):
        """Render templates"""
        ifn = self.ifn
        ofn = self.ofn
        css = self.load_theme(self.theme)
        fonts = self.load_fonts()
        tmplenv = Environment(loader=FileSystemLoader(self.tmplpath))
        slide_tmpl = tmplenv.get_template('index.html')

        if not os.path.splitext(ifn)[1] in self.mdexts:
            raise IOError("invalid Markdown extension")

        with codecs.open(ifn, 'r', encoding='utf-8') as filehandle:
            content = markdown(filehandle.read(),
                               extensions=['markdown.extensions.fenced_code',
                                           'markdown.extensions.codehilite'])
        hlcss = HtmlFormatter().get_style_defs('.codehilite')
        content = content.split('<hr />')
        buf = slide_tmpl.render(css=css,
                                hlcss=hlcss,
                                content=enumerate(content),
                                fonts=fonts)
        with codecs.open(ofn, 'w', encoding='utf-8',
                         errors='xmlcharrefreplace') as filehandle:
            filehandle.write(buf)

    def load_theme(self, theme):
        """Load theme CSS files"""
        filename = os.path.join(self.tmplpath,
                                'themes/{0}.css'.format(theme))
        with open(filename, 'r') as filehandle:
            return filehandle.read()

    def load_fonts(self):
        prefix = os.path.join(self.tmplpath, 'themes/fonts/')
        fonts = []
        for fontfile in os.listdir(prefix):
            font = {}
            font['name'] = os.path.splitext(fontfile)[0]
            with open(prefix + fontfile, 'r') as filehandle:
                font['data'] = base64.b64encode(filehandle.read())
            fonts.append(font)
        return fonts
