#!/usr/bin/env python
# coding=utf-8

import inkex
from tkinter import messagebox

def set_props(elem):
    if len(elem.getchildren()) != 2:
        messagebox.showwarning(
                'Not enough children','Not enough children found. Are you running this on the path?') 
        raise inkex.AbortExtension()

    first_child = elem.getchildren()[0]
    second_child = elem.getchildren()[1]

    elem.attrib['region'] = first_child.attrib['region']
    elem.attrib['long-name'] = first_child.attrib['long-name']
    elem.attrib['short-name'] = first_child.attrib['short-name']
    elem.attrib['value'] = first_child.attrib['value']

    first_child.attrib.pop('region')
    first_child.attrib.pop('long-name')
    first_child.attrib.pop('short-name')
    first_child.attrib.pop('value')

    second_child.attrib.pop('region')
    second_child.attrib.pop('long-name')
    second_child.attrib.pop('short-name')
    second_child.attrib.pop('value')

    if 'style' in second_child.attrib:
        second_child.attrib.pop('style')

    second_child.attrib['map-type'] = 'inset-region'
    
    return True


class setInsetProperties(inkex.EffectExtension):
    def effect(self):
        for selected in self.svg.selected:
            set_props(selected)

if __name__ == '__main__':
    setInsetProperties().run()
