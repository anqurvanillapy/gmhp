#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
import markdown
from jinja2 import *


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
        tmplenv = Environment(loader=FileSystemLoader(self.tmplpath))
        slide_tmpl = tmplenv.get_template('index.html')

        if not os.path.splitext(ifn)[1] in self.mdexts:
            raise IOError("invalid Markdown extension")

        with codecs.open(ifn, 'r', encoding='utf-8') as filehandle:
            content = markdown.markdown(filehandle.read())
        buf = slide_tmpl.render(css=css, content=content)
        with codecs.open(ofn, 'w', encoding='utf-8',
                         errors='xmlcharrefreplace') as filehandle:
            filehandle.write(buf)

    def load_theme(self, theme):
        """Load theme CSS files"""
        filename = os.path.join(self.tmplpath,
                                'themes/{0}.css'.format(theme))
        with open(filename, 'r') as filehandle:
            return filehandle.read()
