#!/usr/bin/env python
# coding=utf-8

import inkex
from tkinter import messagebox

def set_props(elem, prop, value):

    elem.attrib[prop] = value

    return True


class setInsetProperties(inkex.EffectExtension):
    def add_arguments(self, pars):
        pars.add_argument("--property", type=str, help="Property name")
        pars.add_argument("--value", type=str, help="Value to set")

    def effect(self):
        for selected in self.svg.selected:
            set_props(selected, self.options.property, self.options.value)

if __name__ == '__main__':
    setInsetProperties().run()
