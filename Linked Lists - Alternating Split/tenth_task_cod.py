#10
class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError('Your list is empty or to small')
    first = head
    second = head.next
    second_head = second
    curr = second
    while curr and curr.next:
        first.next = curr.next
        first = first.next
        second.next = first.next
        second = second.next
        curr = second
    if first:
        first.next = None

    return Context(head, second_head)
