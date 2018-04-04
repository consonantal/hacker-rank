#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the plusMinus function below.
#
def plusMinus(arr):
    arr_length = len(arr)
    positive_numbers_length = 0
    negative_numbers_length = 0
    zeros_length = 0
    for number in arr:
        if number > 0:
            positive_numbers_length = positive_numbers_length + 1
        elif number < 0:
            negative_numbers_length = negative_numbers_length + 1
        else:
            zeros_length = zeros_length + 1
    print(float(float(positive_numbers_length)/float(arr_length)))
    print(float(float(negative_numbers_length)/float(arr_length)))
    print(float(float(zeros_length)/float(arr_length)))


if __name__ == '__main__':
    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    plusMinus(arr)

