#!/bin/python3

import os
import sys

# Complete the solve function below.
def solve(arr,c=0):
    arr.append(2**64)
    idx, routes = 0, 0
    stack, m = [], {}
    while idx < len(arr):
        if stack == [] or arr[idx] <= stack[-1]:
            stack.append(arr[idx])
            if arr[idx] in m:
                m[arr[idx]] += 1
            else:
                m[arr[idx]] = 1
            idx += 1
        else:
            top = stack.pop()
            if top in m and top < arr[idx]:
                routes += m[top] * (m[top] - 1) 
                del m[top]
    return(routes)
 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = solve(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
