#!/usr/bin/env python
#coding=utf-8

'readTextFile.py -- read and display text file'

#get filename

fname=raw_input('Enter filename:')

#attempt to open file for reading

try:
    fobj=open(fname,'r')
except IOError,e:
    print "*** file open error:",e
else:
    #display contests to the screen 
    for eachLine in fobj:
        print eachLine,
    fobj.close()