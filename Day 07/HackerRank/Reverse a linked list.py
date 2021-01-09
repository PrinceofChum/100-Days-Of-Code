class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
       
def reverse(head):
    prev = None
    while head:
        prev = Node(head.data, prev)
        head = head.next
    return prev
