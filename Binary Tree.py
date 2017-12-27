#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("\nBinary Trees")

class BT(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def is_leaf(self):
        return self.left is None and self.right is None
    
    def insert_left(self,new_node):
        if not self.left:
            self.left = BT(new_node)
        else:
            t = BT(self.left)
            t.left = new_node
            self.left = t
            
    def insert_right(self,new_node):
        if not self.right:
            self.right = BT(new_node)
        else:
            t = BT(self.right)
            t.right = new_node
            self.right = t
            
    def __repr__(self):
        return '{}'.format(self.value)
    
def main():
    tree = BT(1)
    tree.insert_left(2)
    tree.insert_right(3)
    tree.left.insert_left(4)
    tree.left.insert_right(5)
    tree.right.insert_left(6)
    tree.right.insert_right(7)
    assert(tree.right.is_leaf() == False)
    assert(tree.right.right.is_leaf() == True)
    print("\t\t\t",tree)
    print("\t",tree.left,'\t\t\t\t',tree.right)
    print(tree.left.left,'\t\t',tree.left.right,'\t\t',tree.right.left,'\t\t',tree.right.right)

if __name__ == '__main__':
    main()