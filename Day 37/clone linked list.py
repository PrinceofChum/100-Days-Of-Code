#Geeks For Geeks Code

'''Python program to clone a linked list with next and arbitrary pointers'''
'''Done in O(n) time with O(1) extra space'''
  
class Node: 
    '''Structure of linked list node'''
  
    def __init__(self, data): 
        self.data = data 
        self.next = None
        self.random = None
  
def clone(original_root): 
    '''Clone a doubly linked list with random pointer'''
    '''with O(1) extra space'''
  
    '''Insert additional node after every node of original list'''
    curr = original_root 
    while curr != None: 
        new = Node(curr.data) 
        new.next = curr.next
        curr.next = new 
        curr = curr.next.next
  
    '''Adjust the random pointers of the newly added nodes'''
    curr = original_root 
    while curr != None: 
        curr.next.random = curr.random.next
        curr = curr.next.next
  
    '''Detach original and duplicate list from each other'''
    curr = original_root 
    dup_root = original_root.next
    while curr.next != None: 
        tmp = curr.next
        curr.next = curr.next.next
        curr = tmp 
  
    return dup_root 
  
def print_dlist(root): 
    '''Function to print the doubly linked list'''
  
    curr = root 
    while curr != None: 
        print('Data =', curr.data, ', Random =', curr.random.data) 
        curr = curr.next
  
####### Driver code ####### 
'''Create a doubly linked list'''
original_list = Node(1) 
original_list.next = Node(2) 
original_list.next.next = Node(3) 
original_list.next.next.next = Node(4) 
original_list.next.next.next.next = Node(5) 
  
'''Set the random pointers'''
  
# 1's random points to 3 
original_list.random = original_list.next.next
  
# 2's random points to 1 
original_list.next.random = original_list 
  
# 3's random points to 5 
original_list.next.next.random = original_list.next.next.next.next
  
# 4's random points to 5 
original_list.next.next.next.random = original_list.next.next.next.next
  
# 5's random points to 2 
original_list.next.next.next.next.random = original_list.next
  
'''Print the original linked list'''
print('Original list:') 
print_dlist(original_list) 
  
'''Create a duplicate linked list'''
cloned_list = clone(original_list) 
  
'''Print the duplicate linked list'''
print('\nCloned list:') 
print_dlist(cloned_list) 
