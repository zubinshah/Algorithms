#!/usr/bin/python
import sys

if len(sys.argv) is not 3:
    print "Error: Usage :" + sys.argv[0] + "X Y"
else:
    x = sys.argv[1]
    y = sys.argv[2]

xored = int(x) ^ int(y)

num1s = 0
#print xored
while xored is not 0:
    xored>>=1
    num1s+=1

print str(num1s) + ": bits to be flipped when converting from " + str(x) + " to " + str(y) + "."
