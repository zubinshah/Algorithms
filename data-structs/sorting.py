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
    c, s = 0, 0
    num = len(data)
    if debug is True:
        print "Data Length : " + str(num)

    for i in xrange(0, num):
        curr_min = i
        newMin = False
        for j in xrange(i+1, num):
            c += 1
            if data[j] < data[curr_min]:
                curr_min = j
                newMin = True
        if newMin is True:
            s += 1
            data[i] , data[curr_min] = data[curr_min], data[i]
    return [c, s]        
#******************************************************************************

#******************************************************************************
def bubble_sort(data):
    c, s = 0, 0

    num = len(data)
    for i in range(0, num):
        swap = False
        if debug is True:
            print "\niteration " + str(i)

        for j in range(0, num-i-1):
            c = c + 1
            if data[j+1] < data[j]:
                data[j], data[j+1] = data[j+1], data[j]
                s = s + 1
                swap = True
        if swap is False:
            break
    return [c, s]
    
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


def quick_sort_partition (data, lo, hi, c):
    pivot = hi
    partition = lo
    for i in xrange(lo, hi):
        c[0] += 1
        if data[i] < data[pivot]:
            c[1] += 1
            data[i], data[partition] = data[partition], data[i]
            partition = partition + 1
    c[1] += 1
    data[partition], data[pivot] = data[pivot], data[partition]
    return partition

def quick_sort (data, lo, hi, c=[0,0]):
    if lo < hi : 
        p = quick_sort_partition (data, lo, hi, c)
        quick_sort(data, lo, p-1, c)
        quick_sort(data, p+1, hi, c)
    return c

#******************************************************************************

#******************************************************************************
## implement in-place merge routine for merge_sort
def merge_inplace_merge(data, low, mid, high, c):
    i = low
    j = mid
    while i < j and j <= high:
        c[0] += 1
        if data[i] < data[j]:
            i = i + 1
        else:
            c[1]+=1
            data[i], data[j] = data[j], data[i]
            i = i + 1
        if i == j:
            j = j + 1
            i = low

    #middle = mid
    #for j in xrange(mid, high+1):
    #    for i in xrange(low, middle):
    #        if middle <= high:
    #            if data[i] > data[j]:
    #                print "swap", i, data[i], j, data[j], middle
    #                data[i], data[j] = data[j], data[i]
    #                middle = middle + 1
    #return

## Implementing in-place merge sort. Space optimized.
def merge_sort (data, lo, hi, c=[0,0]):
    if (lo < hi):
        mid = (lo + hi + 1) / 2
        merge_sort (data, lo, mid-1, c)
        merge_sort (data, mid, hi, c)

        merge_inplace_merge(data, lo, mid, hi, c)
    return c
#******************************************************************************
#******************************************************************************

def insertion_sort (data):
    c, s = 0, 0
    for i in xrange(1, len(data)):
        #insert elem data[i] at right location and shuffling
        s += 1
        item = data[i]
        j = i
        while j > 0:
            #scan back from j by shifting
            c+=1
            if data[j-1] > item:
                s+=1
                data[j] = data[j-1]
                j -= 1  #location not found, keep shuffling
            else:
                data[j] = item  #copy item at right location
                break
            
            if j == 0:
                data[j] = item
    return [c, s]

#******************************************************************************
def heapsort_heapify(data, num, i, c):
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < num and data[left] > data[largest]:
        largest = left

    if right < num and data[right] > data[largest]:
        largest = right

    c[0] += 2 #two comparisions done above
    if i is not largest:
        
        data[i], data[largest] = data[largest], data[i]
        c[1] += 1 #one comparision done above
        heapsort_heapify(data, num, largest, c)

    return c

def heapsort (data):
    num = len(data)
    c = [0, 0]

    # build a MAXHEAP on the data set in place
    # assuming the array is a binary heap, but needs heapification
    # rightmost node in the second-last level 
    for i in xrange (num/2 - 1,-1, -1):
        heapsort_heapify(data, num, i, c)

    # make a max heap out of the array
    # pick the max everytime and shift with the rightmost
    for i in xrange(num-1, -1, -1):
        data[i], data[0] = data[0], data[i]
        c[1] += 1
        heapsort_heapify(data, i, 0, c)
    return c

#******************************************************************************

#******************************************************************************
def main (num):
    ###########################################################################

    output = {}
            # Key : 'name of sorting algorithm'
            # Values : List of [time , [comparisions, swaps], description

    print "SORTING " + str(num) + " ENTRIES\n"

    ###########################################################################
    print "HEAP SORT"
    data = [int(random.random()*100) for i in xrange(num)]
    t1 = time.time()
    c = heapsort(data)
    t2 = time.time()
    output['heapsort_unsorted'] = [t2-t1, c, "heapsort on unsorted data"]
    ##########
    t1 = time.time()
    c = heapsort(data)
    t2 = time.time()
    output['heapsort_sorted'] = [t2-t1, c, "heapsort on sorted data"]
    ##########
    data.reverse()
    t1 = time.time()
    c = heapsort(data)
    t2 = time.time()
    output['heapsort_worstcase'] = [t2-t1, c, "heapsort on reverse sorted data"]
    ###########################################################################
    print "BUBBLE SORT"
    data = [int(random.random()*100) for i in xrange(num)]
    t1 = time.time()
    c = bubble_sort(data)
    t2 = time.time()
    output['bubble_unsorted'] = [t2-t1, c, "bubble sort on unsorted data"]
    ##########
    t1 = time.time()
    c = bubble_sort(data)
    t2 = time.time()
    output['bubble_sorted'] = [t2-t1, c, "bubble sort on sorted data"]
    ##########
    data.reverse()
    t1 = time.time()
    c = bubble_sort(data)
    t2 = time.time()
    output['bubble_worstcase'] = [t2-t1, c, "bubble sort on reverse sorted data"]
    ###########################################################################
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
    ###########################################################################
    print "SELECTION SORT"
    data = [int(random.random()*100) for i in xrange(num)]
    t1 = time.time()
    c = sel_sort(data)
    t2 = time.time()
    output['selection_unsorted'] = [t2-t1, c, "selection sort on unsorted data"]
    ##########
    t1 = time.time()
    c = sel_sort(data)
    t2 = time.time()
    output['selection_sorted'] = [t2-t1, c, "selection sort on sorted data"]
    ##########
    data.reverse()
    t1 = time.time()
    c = sel_sort(data)
    t2 = time.time()
    output['selection_worstcase'] = [t2-t1, c, "selection sort on reverse sorted data"]
    ###########################################################################
    print "QUICK SORT"
    data = [int(random.random()*100) for i in xrange(num)]
    t1 = time.time()
    c = quick_sort(data, 0, len(data) - 1)
    t2 = time.time()
    output['quick_unsorted'] = [t2-t1, c, "quick sort on unsorted data"]
    t1 = time.time()
    c = quick_sort(data, 0, len(data) - 1)
    t2 = time.time()
    output['quick_sorted'] = [t2-t1, c, "quick sort on unsorted data"]
    data.reverse()
    t1 = time.time()
    c = quick_sort(data, 0, len(data) - 1)
    t2 = time.time()
    output['quick_worstcase'] = [t2-t1, c, "quick sort on reverse sorted data"]
    ########################################################################### 
    print "MERGE SORT"
    data = [int(random.random()*100) for i in xrange(num)]
    t1 = time.time()
    merge_sort(data, 0, len(data) - 1)
    t2 = time.time()
    output['mergesort_unsorted'] = [t2-t1, c, "mergesort on unsorted data"]
    t1 = time.time()
    merge_sort(data, 0, len(data) -1)
    t2 = time.time()
    output['mergesort_sorted'] = [t2-t1, c, "mergesort on sorted data"]
    data.reverse()
    t1 = time.time()
    merge_sort(data, 0, len(data)-1)
    t2 = time.time()
    output['mergesort_worstcase'] = [t2-t1, c, "mergesort on reverse sorted data"]
    ########################################################################### 
    print "INSERTION SORT"
    data = [int(random.random()*100) for i in xrange(num)]
    t1 = time.time()
    c = insertion_sort(data)
    t2 = time.time()
    output['insertionsort_unsorted'] = [t2-t1, c, "insertion sort on unsorted data"]
    t1 = time.time()
    c = insertion_sort(data)
    t2 = time.time()
    output['insertionsort_sorted'] = [t2-t1, c, "insertion sort on sorted data"]
    data.reverse()
    t1 = time.time()
    c = insertion_sort(data)
    t2 = time.time()
    output['insertionsort_worstcase'] = [t2-t1, c, "insertion sort on reverse sorted data"]
    ###########################################################################

    #TBD : format output 
    print output
    return 
#******************************************************************************

#******************************************************************************
main(1000)
#******************************************************************************
