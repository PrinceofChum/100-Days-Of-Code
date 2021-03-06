import sys

n, q = input().strip().split(' ')
n, q = [int(n), int(q)]
number = list(map(int, input().strip().split(' ')))

# get the prime numbers
lower = 2
upper = 10000
prime = [i for i in range(lower, upper + 1) if all(i % j != 0 for j in range(2, i))]

# set Two-dimensional array
A = [[] for i in range(q + 1)] 
B = [[] for i in range(q + 1)] 
A[0] = number

# pick up plates from A stack
for i in range(q):
    for j in range(len(A[i])):
        n = A[i].pop()
        if n % prime[i] == 0:
            B[i].append(n)
        else :
            A[i+1].append(n)
            
# print plates in B
for i in range(len(B)):
    while B[i] != []:
        print(B[i].pop(),)
        
# print plates in A
for i in range(len(A)):
    while A[i] != []:
        print(A[i].pop(),)
