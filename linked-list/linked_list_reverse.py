class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    

a = Node(12)
b = Node(34)
c = Node(27)

a.next = b
b.next = c

def reverse(head):
    curr = head
    prev = None

    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev


print(reverse(a))