def rotateLeft(d, arr):
    n=1
    while n<=d:
        dort=arr.pop(0)
        arr.append(dort)
        n+=1
    return arr
