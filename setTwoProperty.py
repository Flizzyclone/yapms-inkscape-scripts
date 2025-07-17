#!/usr/bin/env python
# coding=utf-8

import inkex
from tkinter import messagebox

def set_props(elem, prop, value, prop2, value2):

    elem.attrib[prop] = value

    elem.attrib[prop2] = value2

    return True


class setInsetProperties(inkex.EffectExtension):
    def add_arguments(self, pars):
        pars.add_argument("--property", type=str, help="Property name 1")
        pars.add_argument("--value", type=str, help="Value to set 1")
        pars.add_argument("--property2", type=str, help="Property name 2")
        pars.add_argument("--value2", type=str, help="Value to set 2")

    def effect(self):
        for selected in self.svg.selected:
            set_props(selected, self.options.property, self.options.value, self.options.property2, self.options.value2)

if __name__ == '__main__':
    setInsetProperties().run()
