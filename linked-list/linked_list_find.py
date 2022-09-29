class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    

a = Node(12)
b = Node(34)
c = Node(27)

a.next = b
b.next = c

def linked_list_find(head, target):
  arr = []
  curr = head
  
  while curr is not None:
    arr.append(curr.val)
    if target in arr:
      return True
    curr = curr.next
  return False

def recur_find(head, target):
    if head == None:
        return False
    if head.val == target:
        return True
    return recur_find(head.next, target)

print(linked_list_find(a, 27))
print(linked_list_find(a, 34))
