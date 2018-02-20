#!/usr/local/bin/python

"""
HEAP Data Structure

Binary Heap : is a ocmplete binary tree which satisfies the heap property.

General heap data structure, is represented as a complete binary tree, which specifies a specific heap (max-heap or min-heap) property.
    * not a sorted structure
    * partially structured

Heap with n nodes
Has a height of Log(n)
Common application of heap is to implement a priority queue

Common implementation : is to use Array Implementation. This lets the array be 
implemented as a binary heap with level order traversal in an array. Some 
implementations skip index 0 for convenience.

    * Node n
    * Left child index = 2*n + 1
    * Right child index = 2*n + 2
    * Parent's index = n/2

Typical Operations: 
    * insert()
    * deletemin (*)
    * delete (*)
    * heapsort
"""
import random

class BinaryHeap:
    heap = []
    count = 0

    def __init__ (self, num):
        #reserving index 0, for dummy heap node
        self.heap = [None for i in xrange(num+1)]
        self.count = 0

    def size(self):
        if self.count != len(self.heap):
            print "Erorr.. "

        return self.count

    def display (self):
        print self.heap
   
    def insert(self, item):
        idx = self.count + 1

        self.heap[idx] = item
        curr = idx
        parent = curr/2
    
        while parent > 0:
            if self.heap[parent] > self.heap[curr]:
                self.heap[parent],self.heap[curr] = self.heap[curr],self.heap[parent]
                curr = parent
                parent = parent/2
            else:
                break
        self.count += 1     #inc total counts in the heap
        return
                
        #self.heap[self.count] = item

        #curr = self.count
        #parent = curr/2
        #
        #while (curr != parent):
        #    if self.heap[parent] > self.heap[curr]:
        #        self.heap[parent],self.heap[curr] = self.heap[curr],self.heap[parent]
        #        curr = parent
        #        parent = curr/2
        #    else:
        #        break
        #
        #self.count += 1 #increment total counts in the heap
        #return 

    def checker(self, root):
        curr = root
        left = 2*curr
        right = 2*curr + 1

        if left < self.count:
            #if self.heap[curr] > self.heap[left]:
            if self.heap[left] < self.heap[curr]:
                print "Checker error.. left", curr, left, right
    
        if right < self.count:
            #if self.heap[curr] > self.heap[right]:
            if self.heap[right] < self.heap[curr]:
                print "Checker error.. right", curr, left, right
                 
        if left < self.count :
            self.checker(left)

        if left < self.count :
            self.checker(right)

    def delete(self):
        if self.count is 0:
            return None

        #remove minimum element from the list 
        item = self.heap[1]

        #maintain heap property by percolating down, copy last index
        self.heap[1] = self.heap[self.count]    #index is 1 based
        self.heap[self.count] = None

        curr = 1
        left = 2*curr
        right = 2*curr + 1

        while left < self.count or right < self.count:
            smallest = curr
            if left < self.count and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < self.count and self.heap[right] < self.heap[smallest]:
                smallest = right
           
            if smallest != curr: 
                self.heap[smallest], self.heap[curr] = self.heap[curr],self.heap[smallest]
                curr = smallest
                left = 2*curr
                right = 2*curr + 1
            else:
                break

        self.count -= 1
        return item

def main(num):
    bHeap = BinaryHeap(num)

    for i in xrange(num):
        bHeap.insert(int(random.random()*100))

    #bHeap.display()
    bHeap.checker(1)

    ## try to introduce error in the heap to verify 
    #bHeap.heap[1024] = 0
    #bHeap.heap[524] = 0
    
    
    prev , curr = None, None
    for i in xrange(num):
        curr = bHeap.delete()
        if prev is not None:
            if (prev > curr):
                print "error.. ", prev, curr
        prev = curr

    #bHeap.display()
    print bHeap.heap.count(None)

##############################################################################
main(1024)




""" 

Binomial Heap - Extension to binary heap, and it provides faster merges, union, 
including the operations provided by the binary heaps.
""" 
