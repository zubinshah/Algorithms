#!/usr/bin/python

# PROBLEM STATEMENT
# WRITE A FUNCTION TO FIND IF A NUMBER IS A PALINDROME
import sys


def isPalindrome(number):
	if (number < 10):
		return True
	num = number
	rev = 0;
	while num > 0:
		rev = (rev * 10) + (num % 10)
		num = num/10
	return (number == rev)

maxnum = 100
for n in range (maxnum):
	if isPalindrome(n) is True:
		print str(n) + ",",

print
print
print "Are palindrome numbers less than " + str(maxnum)
print
