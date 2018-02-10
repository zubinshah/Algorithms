#!/usr/local/bin/python

"""
## QUEUE USING STACK and STACK USING QUEUE
QUEUE using a stack 
    + Implement queue algorithm using 2 stacks and implement a queue class
      with test inputs.

STACK using a queue
    + Implement stack algorithm using 2 queues and implement a stack class 
      with test inputs.

STACK AND QUEUE with a Linked-List 
    + Not implemented, but logic described below.

Note that in both these implementation i am using a python list with its standard
library implementations of pop and append. Although not optimized it serves the  purpose.

Class Queue -- implements regular queue using a list data structure in python
Class Stack -- implements regular stack using a list data structure in python
Class Queue1 -- implements a queue using 2 stacks
Class Stack1 -- implements a stack using 2 queue
"""

class Queue:
    """ A simple list based QUEUE implementation in Python """
    def __init__(self):
        self.l = []

    def isEmpty(self):
        if len(self.l) is 0:
            return True
        else:
            return False
        
    def enqueue(self, elem):
        self.l.append(elem)

    def dequeue(self):
        return self.l.pop(0)

    def front(self):
        return self.l[0]

    def back(self):
        return self.l[len(self.l) - 1]

    def clear(self):
        self.l = []

class Stack:
    """ A simple list based STACK implementation in Python """
    def __init__ (self):
        self.stack = []

    def isEmpty(self):
        if len(self.stack) is 0:
            return True
        else:
            return False

    def push (self, elem):
        self.stack.append(elem)

    def pop(self):
        if len(self.stack) is 0:
            return None
        return self.stack.pop()
        
    def top (self):
        return self.stack[len(self.stack) - 1]

    def clear(self):
        self.stack = []

class Queue1:
    """A queue container that is implemented using two stack """
    def __init__(self, depth=None):
        if depth is None:
            maxdepth = 16
        else:
            maxdepth = depth
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, elem):
        self.stack1.push(elem)

    def dequeue(self):
        while (self.stack1.isEmpty() is False):
            self.stack2.push(self.stack1.pop())
        elem = None
        elem = self.stack2.pop()
        while (self.stack2.isEmpty() is False):
            self.stack1.push(self.stack2.pop())
        return elem 

    def isEmpty(self):
        return self.stack1.isEmpty()

    def front(self):
        while (self.stack1.isEmpty() is False):
            self.stack2.push(self.stack1.pop())
        elem = None
        elem = self.stack2.top()
        while (self.stack2.isEmpty() is False):
            self.stack1.push(self.stack2.pop())
        return elem

    def back(self):
        return self.stack1.top()

    def clear (self):
        return self.stack1.clear()

class Stack1:
    """ A stack container that is implemented using two queues """ 
    def __init__ (self):
        self.q1 = Queue()
        self.q2 = Queue()

    def isEmpty(self):
        return self.q1.isEmpty()

    def push (self, elem):
        self.q1.enqueue(elem)
        while (self.q2.isEmpty() is not True):
            self.q1.enqueue(self.q2.dequeue())

        while (self.q1.isEmpty() is not True):
            self.q2.enqueue(self.q1.dequeue())
    
        print self.q1.l
        print self.q2.l

    def pop(self):
        if self.q2.isEmpty() is not True:
            return self.q2.dequeue()
        else:
            return None
        
    def top (self):
        return self.q1.front()

    def clear(self):
        q1.clear()
        q2.clear()


## Test inputs for pushing 5000 numbers 

q = Queue1()
for i in xrange(1000):
    q.enqueue(32)

while q.isEmpty() is not True:
    q.dequeue()

#q = Queue1()
#q.enqueue(1)
#q.enqueue(2)
#q.enqueue(3)
#q.enqueue(4)
#q.enqueue([1,2,3])
#q.enqueue({1,2,3,4})
#
#print q.dequeue()
#print q.dequeue()
#print q.dequeue()
#print q.dequeue()
#print q.dequeue()
#print q.dequeue()
#print q.dequeue()
#
#
#print "stacks ---- "
#s = Stack1()
#s.push(1)
#s.push(2)
#s.push(3)
#s.push(4)
#s.push([1,1])
#s.push({1,2,3})
#
#print "stack pop" 
#print s.pop()
#print s.pop()
#print s.pop()
#print s.pop()
#print s.pop()
#print s.pop()
#
#

