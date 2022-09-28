

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    

a = Node(12)
b = Node(34)
c = Node(27)

a.next = b
b.next = c

#iterative
def linked_list_values(head):
    arr = []
    curr = head

    while curr is not None:
        arr.append(curr.val)
        curr = curr.next
    return arr


print(linked_list_values(a))


#recursive
def list_values(head):
    values = []
    count_list(head, values)
    return values

def count_list(head, values):
    if head is None:
        return
    values.append(head.val)
    return count_list(head.next, values)

print(list_values(a))