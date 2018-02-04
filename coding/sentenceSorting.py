#!/usr/bin/python

# parse a string and store each word in an array : in sorted order.
# parse a sentence, store every word of the sentence in a sorted order.


import sys


line = sys.stdin.readline()
line = line.split()

for words in line : 
    print words
    #add words for each line in a sorted array, with the position of each word 

#print "Enter the sentences to be parsed, and when done type \"done\" to end." 
#
#lines = []
#while (1):
#    line = sys.stdin.readline()
#    if (line == "done\n"):
#        break
#    else:
#        lines.append(line)
#
#    
#
#print lines
