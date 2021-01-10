def insertNodeAtPosition(head, data, position):
    x = SinglyLinkedListNode(data)
    if (position == 0):
        head = x
        return head
    c = 1
    itr = head
    while (itr.next != None):
        if (c == position):
            x.next = itr.next
            itr.next = x
            return head
        itr = itr.next
        c +=1
