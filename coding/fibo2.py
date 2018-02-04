#!/usr/bin/python
import sys

#This python program implements fibonacci series of a given function. 

def fibo(n): #print fibo series upto n
    """Print fibonacci series up to n numbers. """
    a, b = 0, 1
    fibSeq = []
    while a < n: 
        fibSeq.append(a)
        a , b = b, a+b
    print fibSeq


if len(sys.argv)==1:
    fibo(1000)
else:
    fibo(int(sys.argv[1]))

