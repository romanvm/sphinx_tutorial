# coding: utf-8
# Created on: 08.01.2016
# Author: Roman Miroshnychenko aka Roman V.M.
# E-mail: romanvm@yandex.ua
"""
Example module for Sphinx tutorial

This module illustrates how to document various
Python objects
"""

import tkinter as tk
import tkinter.ttk as ttk

#: Pi constant
PI = 3.141592654
E = 2.718281828459  #: e constant
example = PI * E
"""Another example of variable documentation"""


def division(divident, divisor):
    """
    Division function

    This is an example of function documentation.
    It illustrates how to document parameters, return values
    and their types, and also the exception that a function
    or a module may raise under certain conditions.

    :param divident: operation divident
    :type divident: float
    :param divisor: operation divisor
    :type divisor: float
    :return: division result
    :rtype: float
    :raises: :class:`ZeroDivisionError` when divisor = 0

    .. note:: This function can accept :class:`int` parameters too.

    .. warning:: ``divisor=0`` will cause :class:`ZeroDivisionError` exception!

    Example::

        result = division(a, b)
    """
    return divident / divisor


class Application(tk.Frame):
    """
    A very simple GUI application

    This example illustrates writing docstrings for a class.

    :param master: a master Tkinter widget (opt.)

    Example::

        app = Application()
    """
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack(padx=5, pady=5)
        self._create_widgets()

    def _create_widgets(self):
        self._label = ttk.Label(self, text='Hello World!', width=30, anchor='center')
        self._label.pack()
        self._quit_btn = ttk.Button(self, text='QUIT', command=root.destroy)
        self._quit_btn.pack()

    def get_text(self):
        """
        Get label text

        This is an example of a method docstring

        :return: label text
        :rtype: str
        """
        return self._label['text']

    def set_text(self, value):
        """
        Set label text

        This is another example of a method docstring

        :param value: new label text
        :type value: str
        """
        self._label['text'] = value


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    app.mainloop()
