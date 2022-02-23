#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    denominator = n
    new_arr = []
    neg_count = 0
    zero_count = 0
    pos_count = 0
    for i in arr:
        if i < 0:
            neg_count = neg_count + 1
        elif i == 0:
            zero_count = zero_count + 1
        else:
            pos_count = pos_count + 1
    pos = format(pos_count/denominator, ".6f")
    neg = format(neg_count/denominator, ".6f")
    zero = format(zero_count/denominator, ".6f")
    print(pos)
    print(neg)
    print(zero)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
