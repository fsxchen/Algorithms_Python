from link_list import SingleLinkList, Node


def reserve_single_link_list(linklist: SingleLinkList):
    if linklist.head == None:
        return
    pre = None
    cur = linklist.head
    while cur:
        next_node = cur.next
        cur.next = pre

        pre = cur
        cur = next_node

    linklist.head = pre


if __name__ == "__main__":
    s = SingleLinkList()
    s.build_with_list([1, 2, 3])
    s.print()
    new_head = reserve_single_link_list(s)
    s.print()
