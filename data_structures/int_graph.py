#!/usr/bin/python
'''
    int_graph module is a wrapper module to implement an integer graph data 
    structure in python.
    TBD : 
        (1) derive child class to differentiate matrix vs adj-list impl.
        (2) dynamically grow/shrink the graph data struct (matrix) and avoid
            constructor to specific max nodes for matrix implementation
        (3) 
'''

print "Importing integer graph module."

from collections import deque

class IntGraph:
    """A base class defined for a graph data structures and utilities """

    nodes = []

    #constructor 
    def __init__(self, max_nodes):
        self.nodes = [[0 for i in range(max_nodes)] for i in range(max_nodes)]

    def add_edge(self, from_v, to_v):
        self.nodes[from_v][to_v] = 1
       
    def debug_print_graph(self):
        print "DEBUG : printing self.nodes" 
        print self.nodes       

    def breadth_first_traversal(self, root, debug=0):
        """breadth first traversal for graph """
        queue = deque()
        visited = [0 for i in range(len(self.nodes))]

        #add an item to the end of the list(queue operation)
        queue.append(root)  
         
        while len(queue) is not 0:

            #always dequeue at the front of the list (enqueue operation)
            current = queue.popleft()

            #mark current as visited 
            visited[current] = 1

            #visited!!! 
            if debug is not 0:
                print current

            #traverse all neighbors of current and add them to queue
            for i in range(len(self.nodes[current])):
                if self.nodes[current][i] is not 0:
                    #if i not in visited:
                    if visited[i] == 0:
                        queue.append(i)


    def depth_first_traversal_preorder_iterative (self, root, debug=0):
        """ depth first traversal for graphs (non-recursive) and preorder """
        #using python lists as a stack 
        stack = []

        #maintain a visited array to mark them as visited 
        visited = [0 for i in range(len(self.nodes))]

        #count to check how many nodes were visited
        count=0

        #append root to the stack 
        stack.append(root)

        while len(stack) is not 0:

            current = stack.pop()

            if visited[current] == 1:
                continue

            #preorder traversal for graph
            visited[current] = 1
            if debug == 1:
                print current
            count = count + 1

            #append all neighbors to the stack 
            for i in range (len(self.nodes[current])):
                if self.nodes[current][i] is not 0:
                    if visited[i] is 0:
                        stack.append(i)
                        if debug == 1:
                            print "DEBUG: Append " + str(i) + ", for curr " + str(current)
        if debug == 1:
            print "Total nodes traversed " + str(count) + "."
                
    def depth_first_traversal_non_recursive(self, root, debug=0):
        """depth first travesal for graph NON_RECURSIVE """
        print "TODO" 


#TODO(zubin) : implement an efficient queue operation in python
#TODO(zubin) : implement bft , traversal operation argument
# default is to print for now
