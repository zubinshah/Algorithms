#!/usr/local/bin/python
'''
    Task : Calculate the hourglass sum for every hourglass in a matrix represented by a map
    Once you go through the complete hourglass, then print the maximum hourglass sum

    INput : 6 lines of matrix, separated by spaces
    Output : max hour glass sum
'''

import sys

arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)

ans=[]
for i in xrange(4):
    for j in xrange(4):
        ans.append(arr[i][j+0] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j+0] + arr[i+2][j+1] + arr[i+2][j+2])


print max(ans)
