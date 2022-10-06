
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



def zipper_lists(head_1, head_2):
  tail = head_1
  curr_1 = head_1.next
  curr_2 = head_2
  count = 0
  
  while curr_1 is not None and curr_2 is not None:
    
    if count % 2 == 0:
      tail.next = curr_2
      curr_2 = curr_2.next
    else:
      tail.next = curr_1
      curr_1 = curr_1.next
      
    tail = tail.next
    count += 1
    
  if curr_1 is not None:
    tail.next = curr_1
  if curr_2 is not None:
    tail.next = curr_2
      
  return head_1


print(zipper_lists(a,ab))