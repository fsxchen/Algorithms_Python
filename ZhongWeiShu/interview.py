
class Node:
    next = None
    val = None

def reverse(head):
    # new_head = Node()
    cur = head
    if not cur:
        return
    new_head = None
    while cur:
        new_node = Node(cur.val)
        if not new_head:
            new_head = new_node
        # insert front of new_head
        cur.next = new_head
        new_head = cur

        cur = cur.next
    return new_head

    