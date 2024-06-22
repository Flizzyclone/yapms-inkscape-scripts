#!/usr/bin/env python
# coding=utf-8

import inkex

def set_fill(elem):
    elem.style = 'fill:red;'
    
    return True


class PropogateRedFill(inkex.EffectExtension):

    def effect(self):

        for selected in self.svg.selected:
            set_fill(selected)

if __name__ == '__main__':
    PropogateRedFill().run()
