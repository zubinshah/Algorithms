#!/usr/local/bin/python


list1 = [13, 34, 60, 100, 101, 105]
list2 = [3, 35, 63, 66, 90,102]

def merge_lists(list1, list2):
    total = len(list1) + len(list2)
    newlist = [None for i in xrange(total)]
    i = 0
    j = 0
    idx = 0

    while idx < total:
        print i, j, idx
        if i >= len(list1):
            newlist[idx] = list2[j]
            j+=1
        elif j >= len(list2):
            newlist[idx] = list1[i]
            i+=1
        else:
            if list1[i] < list2[j]:
                newlist[idx] = list1[i]
                i += 1
            else:
                newlist[idx] = list2[j]
                j += 1
        idx += 1

    return newlist

print merge_lists(list1, list2)
# prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
