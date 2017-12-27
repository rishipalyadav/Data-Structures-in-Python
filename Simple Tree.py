#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("\nSimple Trees\n")
class SimpleTree(object):
    def __init__(self, value = None, children = []):
        self.children = children
        self.value = value
        
    def __repr__(self, level = 0):
        ret = "\t"*level+repr(self.value)+"\n"
        for child in self.children:
            ret += child.__repr__(level+1)
        return ret
    
def main():
    st = SimpleTree('a', [SimpleTree('b', [SimpleTree('d'),
       SimpleTree('e')] ), SimpleTree('c', [SimpleTree('h'),
       SimpleTree('g')]) ])
    print(st)
    
if __name__ == '__main__':
    main()