def reversePrint(head):
    itr=head
    lst=[]
    while itr:
        lst.insert(0,itr.data)
        itr=itr.next
    for i in lst:
        print(i)
