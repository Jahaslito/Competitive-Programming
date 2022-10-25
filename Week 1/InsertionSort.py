#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    unsortedElement = arr[n - 1]
    #print(unsortedElement)
    for i, j in reversed(list(enumerate(arr))):
       if j > unsortedElement:
       # print(i+1)
        arr[i+1] = j
        #print(arr[i])
        print(*arr)
       if j < unsortedElement:
        arr[i+1] = unsortedElement
        break
       if i == 0 and j > unsortedElement:
        arr[i] = unsortedElement
         
    print(*arr)
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)