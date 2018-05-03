#!/usr/bin/python

# PROBLEM STATEMENT
import sys



def isPrime (num):
	if (num < 2) : 
		return False;

	for i in range (2, num):
		if (num % i):
			continue;
		else:
			return False;
	return True;

Num= 100
for n in range (Num):
	if isPrime(n) is True:
		print str(n) + " ",

print
print
print "Are prime numbers less than " + str(Num)
print
