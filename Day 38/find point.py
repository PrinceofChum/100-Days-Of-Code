# educaative.io Code

def intersect(head1, head2):
  list1node = None
  list1length = get_length(head1)
  list2node = None
  list2length = get_length(head2)

  length_difference = 0
  if list1length >= list2length :
    length_difference = list1length - list2length
    list1node = head1
    list2node = head2
  else:
    length_difference = list2length - list1length
    list1node = head2
    list2node = head1

  while length_difference > 0:
    list1node = list1node.next
    length_difference-=1

  while list1node != None:
    if list1node == list2node:
      return list1node

    list1node = list1node.next
    list2node = list2node.next
  return None

def get_length(head):
  list_length = 0
  while head != None:
    head = head.next
    list_length+=1
  return list_length

list_head = create_random_list(10)

list_head_1 = create_random_list(5)
list_head_2 = create_random_list(7)
node1 = LinkedListNode(8)
node2 = LinkedListNode(9)

intersect_node = intersect(list_head_1, list_head_2)
assert intersect_node == None, 'intersection found'

insert_at_tail(list_head_1, node1)
insert_at_tail(list_head_1, node2)

insert_at_tail(list_head_2, node1)

print("\nList 1: ")
display(list_head_1)
print("\nList 2: ")
display(list_head_2)

intersect_node = intersect(list_head_1, list_head_2)
print("\nintersect at " + str(intersect_node.data))
assert intersect_node == node1,'incorrect intersection found'
