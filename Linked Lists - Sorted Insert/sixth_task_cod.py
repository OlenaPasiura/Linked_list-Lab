class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def sorted_insert(head, data):
    node1 = Node(data)
    if head is None:
        head = node1
        return node1
    elif data <= head.data:
        node1.next = head
        return node1
    probe = head
    while probe.next is not None:
        if data <= probe.next.data:
            node1.next = probe.next
            probe.next = node1
            return head
        probe = probe.next
    probe.next = node1
    return head
