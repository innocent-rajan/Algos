import sys
import math
import numpy as np


def get_mode(mode_dict):
    mode_count = 0
    mode = 0
    for key, value in mode_dict.items():
        if value > mode_count:
            mode = key
            mode_count = value
        if value == mode_count:
            mode = mode if mode < key else key
    return mode


data = sys.stdin.readlines()
# data = ["10", "64630 11735 14216 99233 14470 4978 73429 38120 51135 67060"]
n = int(data[0])
numbers = sorted([int(x) for x in data[1].split()])

sum = 0
mode_dict = dict()
for number in numbers:
    sum += number
    if number in mode_dict:
        mode_dict[number] += 1
    else:
        mode_dict[number] = 1
if n % 2 == 0:
    median = (numbers[math.floor((n - 1) / 2)] + numbers[int(n / 2)]) / 2
else:
    median = numbers[math.ceil(n / 2)]

mean = sum / n
mode = get_mode(mode_dict)
print(round(mean, 1))
print(round(median, 1))
print(mode)
