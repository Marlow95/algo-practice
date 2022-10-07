
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    

a = Node(12)
b = Node(34)
c = Node(27)

a.next = b
b.next = c

ab = Node(34)
cd = Node(567)

ab.next = cd

def merge_lists(head_1, head_2):
  dummy_head = Node(None)
  tail = dummy_head
  curr_1 = head_1
  curr_2 = head_2
  
  while curr_1 is not None and curr_2 is not None:
    if curr_1.val < curr_2.val:
      tail.next = curr_1
      curr_1 = curr_1.next
    else:
      tail.next = curr_2
      curr_2 = curr_2.next
    tail = tail.next
  
  if curr_1 is not None: tail.next = curr_1
  if curr_2 is not None: tail.next = curr_2
    
  return dummy_head.next

print(merge_lists(a, ab))