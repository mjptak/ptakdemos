#! /lib/python2.6 python
import os
i = 0
while i < 5:
    print "this is just a dummy example file"
    print " this only prints in the branch1 branch"
    i+=1
marklist = os.listdir("/Users/markptak")
os.rename("/Users/markptak/ptakdemos/demo1/two.txt", "/Users/markptak/ptakdemos/demo1/one.txt")
print marklist[0]
