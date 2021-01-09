def compare_lists (llist1, llist2):
    while llist1 and llist2:
        if llist1.data != llist2.data:
            return 0
        else:
            llist1,llist2=llist1.next,llist2.next
    return 1 if llist1 == llist2 else 0
        
