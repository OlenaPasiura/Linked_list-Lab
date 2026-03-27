class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

#3
def push(head, data):
    if head is None:
        node = Node(data)
        node.next = head
    else:
        node = Node(data)
        node.next = head
    return node

def build_one_two_three():
    head = None
    head = push(head, 3)
    head = push(head, 2)
    head = push(head, 1)
    return head
