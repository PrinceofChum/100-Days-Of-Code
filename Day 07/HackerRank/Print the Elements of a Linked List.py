def printLinkedList(head):
    if head:
        print (head.data)
        printLinkedList (head.next)      
