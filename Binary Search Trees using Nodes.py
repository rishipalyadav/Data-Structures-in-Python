#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("\nBinary Search Trees with Nodes")

class Node(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
    def __repr__(self):
        return '{}'.format(self.value)
    
class BSTwithNodes(object):
    def __init__(self):
        self.root = None
        
    def insert(self,value):
        if not self.root :
            self.root = Node(value)
            
        else:
            current = self.root
            while True:
                if value < current.value:
                    if current.left:
                        current = current.left
                        
                    else:
                        current.left = Node(value)
                        break;
                elif value > current.value:
                    if current.right:
                        current = current.right
                        
                    else:
                        current.right = Node(value)
                        break;
                        
                else:
                    break;

def main():
    tree = BSTwithNodes()
    list1 = [4,2,6,1,3,7,5]
    for i in list1:
        tree.insert(i)
    print(tree.root)
    print(tree.root.left)
    print(tree.root.right)
    print(tree.root.left.right)
    print(tree.root.left.left)
    print(tree.root.right.right)
    print(tree.root.right.left)
#    print("\t\t\t",tree.root)
#    print("\n")
#    print("\t",tree.root.left,'\t\t\t\t',tree.root.right)
#    print("\n")
#    print(tree.root.left.left,'\t\t',tree.root.left.right,'\t\t',tree.root.right.left,'\t\t',tree.root.right.right)
if __name__ == '__main__':
    main()
