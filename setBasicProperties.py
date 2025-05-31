#!/usr/bin/env python
# coding=utf-8

import inkex

def set_regions(elem, count):
    elem.attrib['region'] = str(count)
    elem.attrib['short-name'] = str(count)
    elem.attrib['long-name'] = str(count)
    elem.attrib['value'] = '1'
    
    return True


class SetBasicProperties(inkex.EffectExtension):

    def effect(self):
        count = 0
        for selected in self.svg.selected:
            count = count + 1
            set_regions(selected, count)

if __name__ == '__main__':
    SetBasicProperties().run()
