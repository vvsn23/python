#!/usr/bin/python

import pdb

for line in reversed(open("/home/DevOps/file.txt").readlines()):
    print line.rstrip()

