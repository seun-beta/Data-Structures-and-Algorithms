#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    s_unchanged = s[2:8]
    if s[0:2] == "12" and s[8:10] == "PM":
        mil = s[0:2]
        new_mil = mil + s_unchanged
    elif s[0:2] != "12"  and s[8:10] == "PM":
        mil = int(s[0:2]) + 12
        new_mil = str(mil) + s_unchanged
    elif s[0:2] == "12" and s[8:10] == "AM":
        mil = "00"
        new_mil = str(mil) + s_unchanged 
       
    elif s[0:2] != "12" and s[8:10] == "AM":
        mil = s[0:2]
        new_mil = str(mil) + s_unchanged
        print(new_mil)
    return new_mil

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
