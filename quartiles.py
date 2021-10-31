#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quartiles(arr):
    # Write your code here
    arr = sorted(arr)
    print(arr)

    def calc_median(input_arr):
        n = len(input_arr)
        if n % 2 == 0:
            median = (input_arr[math.floor((n - 1) / 2)] + input_arr[int(n / 2)]) / 2
            # median = round(median, 1)
        else:
            median = input_arr[math.floor(n / 2)]
        return median

    arr_len = len(arr)
    if arr_len % 2 == 0:
        q1 = arr[:int(arr_len / 2)]
        q3 = arr[int(arr_len / 2):]
        q1_median = calc_median(q1)
        q3_median = calc_median(q3)
        total_median = calc_median(arr)
        return q1_median, total_median, q3_median
    else:
        q1 = arr[:math.floor(arr_len / 2)]
        q3 = arr[math.ceil(arr_len / 2):]
        print(q1, q3)
        q1_median = calc_median(q1)
        q3_median = calc_median(q3)
        total_median = calc_median(arr)
        return q1_median, total_median, q3_median


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    # data = list(map(int, input().rstrip().split()))
    data = [3, 7, 8, 5, 12, 14, 21, 13, 18]

    res = quartiles(data)
    print(res)

    # fptr.write('\n'.join(map(str, res)))
    # fptr.write('\n')
    #
    # fptr.close()
