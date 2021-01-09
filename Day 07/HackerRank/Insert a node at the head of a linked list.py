class Node(object):
    def __init__(self,data=None,next_node=None):
        self.data=data
        self.next=next_node

def insertNodeAtHead(head, data):
    
    if head:
        return Node(data,head)
    
    head=Node(data)
    return head
