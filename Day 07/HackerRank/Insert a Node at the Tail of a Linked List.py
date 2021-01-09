class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

def insertNodeAtTail(head, data):
    new_node = Node(data)
    if head:
        node = head
        while node.next:
            node = node.next
        node.next = new_node
    else:
        head = new_node
    return head
