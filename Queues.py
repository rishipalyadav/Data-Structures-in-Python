#!/usr/bin/env python3
# -*- coding: utf-8 -*-


print("\nQueue Using Lists:\n")

class Queue(object):
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self,item):
        self.items.insert(0,item)
    
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            raise exception("Queue is Empty")
    def __repr__(self):
       return '{}'.format(self.items)
            
def main():
    q = Queue()
    q.enqueue(1)
    q.enqueue('FSDATYD')
    q.enqueue('W')
    q.enqueue('EFYD')
    print(q.size())
    print(q.peek())
    print(q.dequeue())
    print(q.peek())
    print(q)
if __name__ == '__main__':
    main()
    
    
print("\nQueue Using nodes:\n")

class Node(object):
    def __init__(self,value=None):
        self.value = value
        self.next = None
        
class QueueNodes(object):
    def __init__(self):
        self.front = None
        self.back = None
        
    def isEmpty(self):
        return bool(self.front) and bool(self.back)
    
    def dequeue(self):
        if self.front:
            value = self.front.value
            self.front = self.front.next
            return value
        raise exception("Queue is Empty")
    
    def enqueue(self,value):
        node = Node(value)
        if self.front:
            self.back.next = node
        else:
            self.front = node
        self.back = node
        return True
    
    def size(self):
        node = self.front
        if node:
            num_node = 1
            node = node.next
            while node:
                num_node += 1
                node = node.next
        return num_node
    
    def peek(self):
        return self.front.value

def main():
    q = QueueNodes()
    q.enqueue(1)
    q.enqueue('NODES')
    q.enqueue('W')
    q.enqueue('EFYD')
    print(q.size())
    print(q.peek())
    print(q.dequeue())
    print(q.peek())
    print(q)
if __name__ == '__main__':
    main() 
    
    
print("\nDequeue: \n")

class dequeue(object):
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def addFront(self,item):
        self.items.append(item)
    def addRear(self,item):
        self.items.insert(0,item)
        
    def removeFront(self):
        self.items.pop()
        
    def removeRear(self):
        self.items.pop(0)
        
    def size(self):
        return len(self.items)
    
    def __repr__(self):
       return '{}'.format(self.items)
    
def main():
    dq = dequeue()
    dq.addFront(1)
    dq.addFront(2)
    dq.addFront(3)
    dq.addRear(40)
    dq.addRear(50)
    print(dq.size())
    print(dq)

if __name__ == '__main__':
    main()
