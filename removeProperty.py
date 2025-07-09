#!/usr/bin/env python
# coding=utf-8

import inkex
from tkinter import messagebox

def set_props(elem, prop):
    if prop in elem.attrib:
        elem.attrib.pop(prop)

    return True


class removeProperty(inkex.EffectExtension):
    def add_arguments(self, pars):
        pars.add_argument("--property", type=str, help="Property name")

    def effect(self):
        for selected in self.svg.selected:
            set_props(selected, self.options.property)

if __name__ == '__main__':
    removeProperty().run()
