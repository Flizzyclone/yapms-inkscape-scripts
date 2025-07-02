#!/usr/bin/env python
# coding=utf-8

import inkex
from tkinter import messagebox

def set_props(elem, from_name, to_name):

    elem.attrib[to_name] = elem.attrib[from_name]

    return True


class setInsetProperties(inkex.EffectExtension):
    def add_arguments(self, pars):
        pars.add_argument("--from_name", type=str, help="Property to clone from")
        pars.add_argument("--to_name", type=str, help="Property to clone to")

    def effect(self):
        for selected in self.svg.selected:
            set_props(selected, self.options.from_name, self.options.to_name)

if __name__ == '__main__':
    setInsetProperties().run()
