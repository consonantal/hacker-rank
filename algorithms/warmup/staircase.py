#!/bin/python

from __future__ import print_function

import os
import sys


#
# Complete the staircase function below.
#
def staircase(n):
    for i in range(n):
        print(str(' ' * (n-(i+1))) + str('#' * (i+1)))


if __name__ == '__main__':
    n = int(raw_input())

    staircase(n)

