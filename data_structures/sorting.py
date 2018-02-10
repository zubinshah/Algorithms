#!/usr/local/bin/python
"""
SORTING ALGORITHMS
  + Bubble Sort
  + Selection Sort

This program will test *num* entries as an unsorted array, and sort them as well 
as log the time taken to understand the performances of varous sorting algorithms.
"""

#******************************************************************************
import random
import sys
import time
debug = False

#******************************************************************************
def sel_sort(data):
    t1 = time.time()
    num = len(data)
    if debug is True:
        print "Data Length : " + str(num)

    for i in xrange(0, num):
        curr_min = i
        newMin = False
        for j in xrange(i+1, num):
            if data[j] < data[curr_min]:
                curr_min = j
                newMin = True
                if debug is True:
                    print " .... new min found " + str(data[curr_min])
        if newMin is True:
            data[i] , data[curr_min] = data[curr_min], data[i]
        if debug is True:
            print data
    return (time.time() - t1)
#******************************************************************************

#******************************************************************************
def bubble_sort(data):
    t1 = time.time()
    num = len(data)
    for i in range(0, num):
        swap = False
        if debug is True:
            print "\niteration " + str(i)

        for j in range(0, num-i-1):
            if data[j+1] < data[j]:
                data[j], data[j+1] = data[j+1], data[j]
                swap = True
        if swap is False:
            break
    
    return (time.time() - t1)
#******************************************************************************



#******************************************************************************
def recursive_bubble_sort(data, n):
    if n == 1:
        return
    for i in range(0, n-1):
        if data[i] > data[i+1]:
            data[i], data[i+1] = data[i+1], data[i]
    recursive_bubble_sort(data, n-1)

#******************************************************************************


def quick_sort_partition (data, lo, hi):
    pivot = hi
    partition = lo
    for i in xrange(lo, hi):
        if data[i] < data[pivot]:
            data[i], data[partition] = data[partition], data[i]
            partition = partition + 1
    data[partition], data[pivot] = data[pivot], data[partition]
    return partition

def quick_sort (data, lo, hi):
    if lo < hi : 
        p = quick_sort_partition (data, lo, hi)
        #print "partition " + str(p) + ", lo " + str(lo) + ", hi " + str(hi)
        #print data
        quick_sort(data, lo, p-1)
        quick_sort(data, p+1, hi)

#******************************************************************************


#******************************************************************************
def main (num):
    print "SORTING FOR " + str(num) + " ENTRIES\n"

    print "BUBBLE SORT"
    data = [int(random.random()*100) for i in xrange(num)]
    t = bubble_sort(data)
    print "  Using bubble sort time taken .. " + str(t)
    t = bubble_sort(data)
    print "  Using bubble sort time taken (on sorted array).. " + str(t)

    data.reverse()
    t = bubble_sort(data)
    print "  Using bubble sort time taken (worst case reverse sorted array).. " + str(t)
    
    #print "RECURSIVE BUBBLE SORT"
    #data = [int(random.random()*100) for i in xrange(num)]
    #t = time.time()
    #recursive_bubble_sort(data, len(data))
    #print "  Using recur bubble sort time taken .. " + str(time.time() - t)
    #t = time.time()
    #recursive_bubble_sort(data, len(data))
    #print "  Using recur bubble sort time taken (on sorted array).. " + str(time.time() - t)

    #data.reverse()
    #t = time.time()
    #recursive_bubble_sort(data, len(data))
    #print "  Using recur bubble sort time taken (worst case reverse sorted array).. " + str(time.time() - t)
 
    print "SELECTION SORT"
    data = [int(random.random()*100) for i in xrange(num)]
    t = sel_sort(data)
    print "  Using selection sort time taken .. " + str(t)
    t = sel_sort(data)
    print "  Using selection sort time taken (on sorted array).. " + str(t)
    data.reverse()
    t = sel_sort(data)
    print "  Using selection sort time taken (worst case reverse sorted array).. " + str(t)

    print "QUICK SORT"
    data = [int(random.random()*100) for i in xrange(num)]
    t = time.time()
    quick_sort(data, 0, len(data)-1)
    print "  Using quick sort time taken .. " + str(time.time() - t)
    t = time.time()
    quick_sort(data, 0, len(data)-1)
    print "  Using quick sort time taken (on sorted array).. " + str(time.time() - t)
    data.reverse()
    t = time.time()
    quick_sort(data, 0, len(data)-1)
    print "  Using quick sort time taken (worst case reverse sorted array).. " + str(time.time() - t)

    #print "MERGE SORT"
    #data = [int(random.random()*100) for i in xrange(num)]
    #t = time.time()
    #merge_sort(data)
    #print "  Using merge sort time taken .. " + str(time.time() - t)
    #t = time.time()
    #merge_sort(data)
    #print "  Using quick sort time taken (on sorted array).. " + str(time.time() - t)
    #data.reverse()
    #t = time.time()
    #quick_sort(data, 0, len(data)-1)
    #print "  Using quick sort time taken (worst case reverse sorted array).. " + str(time.time() - t)




main(10240)
