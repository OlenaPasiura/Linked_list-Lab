class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

#2
def linked_list_from_string(list_repr: str) -> Node | None:
    if not list_repr or list_repr == 'None':
        return None
    node = None
    our_lst = list_repr.split(' -> ')
    our_lst = our_lst[::-1]
    if our_lst[0] == 'None':
        our_lst.pop(0)
    for el in our_lst:
        node = Node(int(el), node)
    return node
