#!/bin/python3

import os
import sys
import math

# Complete the solve function below.
def empty(stk):
    return len(stk) == 0

def top(stk):
    if empty(stk):
        return None
    return stk[-1]

def fixStack(stk, h, debug=False):
    prev = None
    count = 0
    res = 0
    while not(empty(stk)) and h > top(stk):
        cur = stk.pop()
        if prev == None:
            count = 1
            prev = cur
        elif prev != None and cur == prev:
            count += 1
            prev = cur
        elif prev != None and cur != prev:
            res += max(0, count * (count - 1))
            count = 1
            prev = cur
    res += max(0, count*(count-1))
    return stk,res
    

def solve(H, debug=False):
    stk = []
    res = 0
    for i,h in enumerate(H):
        if empty(stk) or h <= top(stk):
            stk.append(h)
        elif h > top(stk):
            stk, paths = fixStack(stk, h, debug)
            stk.append(h)
            res += paths
    stk, rem = fixStack(stk, math.inf, debug=False)
    res += rem
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = solve(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
