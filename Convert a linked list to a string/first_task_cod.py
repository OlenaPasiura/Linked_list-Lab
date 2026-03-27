class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

#1
def stringify(node):
    final_str = ''
    if not node:
        return 'None'
    while node != None:
        final_str += str(node.data)
        final_str += ' -> '
        node = node.next
    final_str += 'None'
    return final_str
