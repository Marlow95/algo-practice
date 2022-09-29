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
def sum_of_list(head):
    sum = 0
    curr = head

    while curr is not None:
        sum += curr.val
        curr = curr.next

    return print(sum)

sum_of_list(a)

#recursive
def recur_sum(head):
    if head is None:
        return 0
    return head.val + recur_sum(head.next)


print(recur_sum(a))