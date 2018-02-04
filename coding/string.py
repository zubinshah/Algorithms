#!/usr/bin/python
line1 = "this is a test \n and see how /\n and /' works " 
line2 = "zubin" 
line3 = """zubin

hemantkumar
shah"""

#line = line1 + line2 + line3 
#print line 
#words = line.split()
#print len(words)


def func1 (list1):
    print list1
    cnt = 0
    for i in range(len(list1)):
        cnt = cnt + list1[i]
        list1[i] = list1[i] + 1 
    return cnt


l = [0, 1, 2, 3, 34, 234]
print func1(l)
print func1(l)
