def deleteNode(head, position):
    if position==0:
        head=head.next
        return head
    c=1
    itr=head
    while itr.next!=None:
        if c==position:
            itr.next=itr.next.next
        itr=itr.next
        c+=1    
    return head
