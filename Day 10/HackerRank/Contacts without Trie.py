#!/bin/python3

import os
import sys

#
# as we handle with too many loops, time limit will be exceeded for higher inputs
#
def contacts(queries):
    contacts=[]
    counts=[]
    for partial in queries:
        if partial[0]=='add':
                contacts.append(partial[1])
        if partial[0]=='find':
            maxi=len(partial[1])
            count=0
            for name in contacts:
                if name[:maxi]==partial[1]:
                    count+=1
            counts.append(count)
    return counts                    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    queries_rows = int(input())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    result = contacts(queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
