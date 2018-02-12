#!/usr/bin/python
'''
    test module to test the IntGraph , and other relevant modules
'''

from int_graph import *
import random
import time

def generate_static_connected_graph():
    print "Generating static nodes." 
    gr.add_edge(2, 3)
    gr.add_edge(2, 4)
    gr.add_edge(3, 5)
    gr.add_edge(3, 1)
    gr.add_edge(4, 5)
    gr.add_edge(4, 2)
    gr.add_edge(4, 3)
    gr.add_edge(5, 1)
    gr.add_edge(5, 2)
    gr.add_edge(5, 3)
    gr.add_edge(5, 4)

def generate_random_connected_graph(maxNode):
    print "TODO"

def generate_random_graph (TOTALNODES):
    count = 0

    #for all the nodes in this graph 
    for i in range (TOTALNODES):
        for j in range(random.randint(1, TOTALNODES-1)):
            #add random number of edges from node i to 
            to_node = random.randint(1, TOTALNODES-1)
            if to_node is not i:
                gr.add_edge(i, to_node)
                count = count + 1 
    print "Total random connected edges added " + str(count) + "."


##### 
# MAIN TEST PROGRAM
#####
TOTALNODES = 1000
print "Starting program to create an integer graph with #Nodes " \
            + str(TOTALNODES) + "."
gr = IntGraph(TOTALNODES)

#generate_static_connected_graph()
#generate_random_connected_graph(TOTALNODES)
generate_random_graph(TOTALNODES)

start = time.clock()
gr.breadth_first_traversal(2, 0)
t = (time.clock() - start)
print "Time to execute breadth first traversal: " + str(t)


start = time.clock()
gr.depth_first_traversal_preorder_iterative(2, 0)
t = (time.clock() - start)
print "Time to execute depth first traversal preorder iterative : " + str(t)
