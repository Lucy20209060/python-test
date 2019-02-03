#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os

# print [x*x for x in range(1, 11) if x > 2]

# print [x*x for x in range(1, 11)]

# print [m + n for m in 'ABC' for n in 'XYZ']

# g = (x * x for x in range(11))

# for x in g:
#     print x

def foo():
    print 'step 1'
    yield 1
    print 'step 2'
    yield 2
    print 'step 3'
    yield 3

f = foo()
print f.next()
print f.next()