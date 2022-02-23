#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    lenght = len(arr)
    new_arr = list()
    for i in arr:
        a = sum(arr)-i
        new_arr.append(a)
    print( str(min(new_arr)) + " " + str(max(new_arr)))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
