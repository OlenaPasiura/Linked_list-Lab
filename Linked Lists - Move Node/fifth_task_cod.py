class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

#5
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    if source is None or source.next is None:
        raise ValueError
    first_el = source
    source = source.next
    first_el.next = dest
    return Context(source, first_el)
