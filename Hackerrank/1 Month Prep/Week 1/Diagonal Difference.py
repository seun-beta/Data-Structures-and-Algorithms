#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here

    left_diag = []
    right_diag = []
    count_left = 0

    count_right = int(len(arr)) -1
    for sub_arr in arr:
        
        left_diag.append(sub_arr[count_left])
        
        right_diag.append(sub_arr[count_right])

        count_left = count_left + 1 
        count_right = count_right - 1
    value = abs(sum(left_diag) - sum(right_diag))

    return value
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
