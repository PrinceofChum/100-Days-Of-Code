#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

# Complete the minimumMoves function below.
def minimumMoves(grid, startX, startY, goalX, goalY):
    c=0
    visit=set()
    q=deque([[startX,startY,c]])
    moves=[[1,0],[-1,0],[0,1],[0,-1]]
    
    while q:
        pathx, pathy, c= q.popleft()
        c+=1
        for xi,yi in moves:
            x,y=pathx,pathy
            while True:
                x,y=x+xi,y+yi
                if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y]=='.':
                    if x==goalX and y==goalY:
                        return c
                    elif (x,y) not in visit:
                        visit.add((x,y))
                        q.append([x,y,c])
                else:
                    break
    return -1        
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    startXStartY = input().split()

    startX = int(startXStartY[0])

    startY = int(startXStartY[1])

    goalX = int(startXStartY[2])

    goalY = int(startXStartY[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    fptr.write(str(result) + '\n')

    fptr.close()
