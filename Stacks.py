#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("\nStack Using Lists:\n")
class stack(list):
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    def push(self,items):
        self.items.append(items)
    def pop(self):
        if not self.isEmpty() :
            return self.items.pop()
        else:
            raise exception("Stack is Empty")
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def __repr__(self):
       return '{}'.format(self.items)
    
def main():
    stack_list = stack()
    stack_list.push(4)
    stack_list.push(5)
    stack_list.push(6)
    print(stack_list.size())
    print(stack_list.peek())
    print(stack_list.pop())
    print(stack_list.peek())
    print(stack_list)
if __name__ == '__main__':
    main()

print("\nStack Using nodes:\n")
class Node(object):
    def __init__(self,value = None):
        self.value = value
        self.next = None
    
class StackwithNodes(object):
    def __init__(self):
        self.top = None
    
    def isEmpty(self):
        return bool(self.top)
    
    def pop(self):
        node = self.top
        if node:
            self.top = node.next
            return node.value
        else:
            raise exception("Stack is empty")
        
    def push(self,value):
        node = Node(value)
        node.next = self.top
        self.top = node
    
    def peek(self):
        return self.top.value
        
def main():
    stack = StackwithNodes()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.peek())
    print(stack.pop())
    print(stack.pop())
    print(stack.peek())
    print(stack)
if __name__ == '__main__':
    main()
