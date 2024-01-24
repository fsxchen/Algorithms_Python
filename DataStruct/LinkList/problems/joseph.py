"""
约瑟夫环问题
"""

import os
import sys

cur_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(cur_dir))

from link_list import *

def solve(n, m):
    circul = CircularLinkedList()
    circul.build_with_list(range(1, n + 1))
    circul.print()
    cur = circul.h_node

    # for i in range(1, n + 1):
    #     node = Node(i)
    #     cur.next = node
    #     cur = node
    # # 最后一个指向第一个结点
    # cur.next = head.next
    # return cur.next

    while cur != cur.next:
        for i in range(1, m):
            print("...")
            cur = cur.next
        # 删除下一个的结点
        print("kill %d" % cur.next.value)
        # circul.delete()
        del_node = cur.next
        cur.next = del_node.next
        del del_node
        cur = cur.next
    return cur

if __name__ == "__main__":
    n = 10
    # m = 3
    # l = solve(n, m)
    # print("幸存者", l.value)

    l = solve(n, 2)
    print("幸存者", l.value)