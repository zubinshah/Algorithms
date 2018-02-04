#!/usr/local/bin/python
#Write a function fib() that a takes an integer nn and returns the nth 
#Fibonacci number.

import sys 
import time

def print_usage(name):
    print r"""Usage: \"" + name + " num type\"\
Description: Compute the nth Fibonacci number in the fibonacci series.\
Args: num is the nth fibo number to be computed\
      type represents the type of comptation, recursive, loop, etc.\
        0 compute fibo using a loop\
        1 compute fibo using a recursive implementation\
        2 (default) compute fibo using an optimized recursive implementation\
        3 compute fibo and print the series"""



    #print "Usage: \"" + name + " num type\""
    #print "Description: Compute the nth Fibonacci number in the fibonacci series."
    #print "Args: num is the nth fibo number to be computed"
    #print "      type represents the type of comptation, recursive, loop, etc."
    #print "          0 compute fibo using a loop"
    #print "          1 compute fibo using a recursive implementation" 
    #print "          2 (default) compute fibo using an optimized recursive implementation" 
    #print "          3 compute fibo and print the series"
    
def fibo_recur (n):
    "Calculates fibo by recursively invoking fibo_recur"
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else: 
        return fibo_recur(n-1) + fibo_recur(n-2)

def fibo_recur_wrap (x):
    "Wrapper function to execute fibo_recur to test/print the time taken"
    t0 = time.time()
    fib = fibo_recur (x)
    t1 = time.time()
    print "\n"
    print "Fibo(" + str(x) + "): " + str(fib) + ". (recur without optimization)"
    print "Time : " + str (t1-t0) + " sec."

def fibo_recur2 (n, fibo_list):
    "Calculate fibo by recursively calling and optimizing the recursion, and \
     assumes that the first fibo_list is a list of None"
    
    if fibo_list[n] is not None:
        return fibo_list[n]

    if n == 0:
        fibo_list[n] = 0
    elif n == 1:
        fibo_list[n] = 1
    else:
        fibo_list[n] = fibo_recur2 (n-1, fibo_list) + fibo_recur2 (n-2, fibo_list)

    return fibo_list[n]

def fibo_recur2_wrap (x, print_series):
    "Wrapper function to execute fibo_recur2 to test/print the time taken"
    flist = [None for i in range (x+1)] 
    t0 = time.time()
    fib = fibo_recur2 (x, flist)
    t1 = time.time()

    if print_series is False:
        print "\n"
        print "Fibo(" + str(x) + "): " + str(fib) + ". (recur with optimization)"
        print "Time : " + str (t1-t0) + " sec."
    else :
        print "\n"
        print flist

def fibo_loop (n):
    "Calculate fibo in a for loop" 
    a, b = 0, 0
    for i in range (0, n):
        if i <= 1:
            a , b = 0, 1
        else: 
            a, b = b, a+b

    return a+b
    #print "fibo(" + str(n) + "):" + str(a+b)

def fibo_loop_wrap (x):
    "Wrapper function to execute fibo_loop to test/print the time taken"
    t0 = time.time()
    fib = fibo_loop(x)
    t1 = time.time()
    print "\n"
    print "Fibo(" + str(x) + "): " + str(fib) + ". (loop)"
    print "Time : " + str (t1-t0) + " sec."


def main ():
    """Main function""" 
    num = len(sys.argv)

    '''DEBUG ONLY
    print num
    for i in range (0, num):
        print sys.argv[i]
    print_usage(sys.argv[0])
    '''

    if num == 2: 
        x = int(sys.argv[1])
        fibo_recur2_wrap(x, False)
        return
    elif num == 3: 
        x = int(sys.argv[1])
        xtype = int(sys.argv[2])

        if xtype == 0:
            fibo_loop_wrap(x)
            return
        elif xtype == 1:
            fibo_recur_wrap(x)
            return
        elif xtype == 2:
            fibo_recur2_wrap(x, False)
            return
        elif xtype == 3:
            fibo_recur2_wrap(x, True)
            return

    print_usage(sys.argv[0])

## EXECUTE MAIN FUNCTION 
main()
