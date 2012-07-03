# -*- coding: utf-8  -*-
#
# Copyright (C) 2012 by Ben Kurtovic <ben.kurtovic@verizon.net>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
`mwparserfromhell <https://github.com/earwig/mwparserfromhell>`_ (the MediaWiki
Parser from Hell) is a Python package that provides an easy-to-use and
outrageously powerful parser for `MediaWiki <http://mediawiki.org>`_ wikicode.
"""

__author__ = "Ben Kurtovic"
__copyright__ = "Copyright (C) 2012 by Ben Kurtovic"
__license__ = "MIT License"
__version__ = "0.1.dev"
__email__ = "ben.kurtovic@verizon.net"

from mwparserfromhell.node import Node
from mwparserfromhell.parameter import Parameter
from mwparserfromhell.parser import Parser
from mwparserfromhell.string_mixin import StringMixIn
from mwparserfromhell.template import Template
from mwparserfromhell.text import Text
from mwparserfromhell.wikicode import Wikicode

parse = Parser().parse
