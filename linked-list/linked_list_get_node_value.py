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
def get_node_value(head, index):
    curr = head
    count = 0

    while curr is not None:
        if count ==  index:
            return curr.val
        
        curr = curr.next
        count += 1

    return None


#recursive

def recur_get_node_value(head, index):
    if head is None:
        return None
    if index == 0:
        return head.val

    return recur_get_node_value(head.next, index - 1)

print(get_node_value(a, 2))
print(get_node_value(a, 3))

print(recur_get_node_value(a, 3))
print(recur_get_node_value(a, 1))