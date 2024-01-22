"""
约瑟夫环问题
"""

import os
import sys

cur_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(cur_dir))

from link_list import *

def solve(n=41):
    """
    默认是41个人
    """
    head = Node(0)
    cur = head
    for i in range(1, n + 1):
        node = Node(i)
        cur.next = node
        cur = node
    # 最后一个指向第一个结点
    cur.next = head.next
    return cur.next

if __name__ == "__main__":
    l = solve(n, m)
    m = 3
    while l != l.next:
        for i in range(1, m - 1):
            l = l.next
        # 删除下一个的结点
        print("%d" % l.next.value, end="->")

        del_node = l.next
        l.next = del_node.next
        del del_node
        l = l.next

    print(l.value)