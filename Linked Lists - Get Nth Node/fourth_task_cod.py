class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

#4
# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

def get_nth(node, index):
    if node is None or index < 0:
        raise Exception
    probe = node
    count = 0
    while probe != None:
        if count == index:
            return probe
        probe = probe.next
        count += 1
    raise IndexError
