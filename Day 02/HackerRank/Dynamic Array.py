N,Q = map(int, input().split())
lastAns=0
seq=[]
for i in range(N):
    seq.append([])
    
for queries in range(Q):
    vals= list(map(int, input().split()))
    x,y=vals[1],vals[2] 
    #print lastAns 
    #print seq  
    if vals[0]==1:
        index=(x ^ lastAns) % N
        seq[index].append(y)
        #print index 
    else:
        index=(x ^ lastAns) % N
        size=y % len(seq[index])
        lastAns= seq[index][size]
        print (lastAns)
