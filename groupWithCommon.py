#!/usr/bin/env python
# coding=utf-8

import inkex
from tkinter import messagebox
from lxml import etree

def group(elem):
    parent = elem.getparent()
    if parent.attrib['map-type'] != 'regions':
        messagebox.showwarning(
                'Not child of regions','This path is not an element of regions.') 
        raise inkex.AbortExtension()
    
    parent_children = parent.getchildren()

    id = elem.attrib['id'].partition('-')[0]

    for child in parent_children:
        childid = child.attrib['id']
        if childid == id:
            g = etree.SubElement(parent, inkex.addNS('g','svg'))
            etree.SubElement(g, 'path', child.attrib)
            etree.SubElement(g, 'path', elem.attrib)
            elem.delete()
            child.delete()
            break
    
    return True


class groupWithCommon(inkex.EffectExtension):
    def effect(self):
        for selected in self.svg.selected:
            group(selected)

if __name__ == '__main__':
    groupWithCommon().run()
