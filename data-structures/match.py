#!/usr/local/bin/python


'
Building an IDE, identify only comments in an source code. 
'


import re
import sys

Pattern1 = r'\/\/'
Pattern2 = r'\/\*'
Pattern3 = r'\*\/'

multi_line = False

for line in sys.stdin:
    m1 = re.search(Pattern1, line)
    m2 = re.search(Pattern2, line)
    m3 = re.search(Pattern3, line)
    if m1 is not None:
        print line[m1.start():],
        if (m2 is not None) and (m3 is not None):
            print line[m2.start():m3.end()]
        elif (m2 is not None) and (m3 is None):
            print line[m2.start():],
            multi_line = True
        elif (m2 is None) and (m3 is not None):
            print line[:m3.end()].strip()
            multi_line = False
        elif (m2 is None) and (m3 is None) and (multi_line is True):
            print line.strip()
