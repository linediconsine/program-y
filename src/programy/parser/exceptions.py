"""
Copyright (c) 2016 Keith Sterling

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

class ParserException(Exception):
    def __init__(self, message, filename=None, xml_exception=None, xml_element=None):
        self._message = message
        self._filename = filename
        self._xml_exception = xml_exception
        self._xml_element = xml_element

    @property
    def message(self):
        return self._message

    @property
    def filename(self):
        return self._filename

    def format_message(self):
        msg = self._message

        if self._filename is not None:
            msg += " in [%s]" % self._filename

        if self._xml_exception is not None:
            msg += " at [line(%d), column(%d)]" % (self._xml_exception.position[0],
                                                   self._xml_exception.position[1])

        if self._xml_element is not None:
            if hasattr(self._xml_element, '_end_line_number') and hasattr(self._xml_element, '_end_column_number'):
                msg += " at [line(%d), column(%d)]" % (self._xml_element._end_line_number,
                                                       self._xml_element._end_column_number)
        return msg

class MatcherException(Exception):
    def __init__(self, message):
        self.message = message