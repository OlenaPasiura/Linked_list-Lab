#9
def swap_pairs(head):
    if head is None or head.next is None:
        return head
    probe = head
    prev = None
    before_pair = None
    count = 0
    while probe is not None:
        count += 1
        if count == 2:
            first = prev
            second = probe

            first.next = second.next
            second.next = first
            if before_pair is None:
                head = second
            else:
                before_pair.next = second
            before_pair = first
            probe = first.next
            count = 0
        else:
            prev = probe
            probe = probe.next

    return head
