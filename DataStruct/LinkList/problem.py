from _typeshed import StrPath
from single_link_list import SingleLinkList, Node


class LinkList(SingleLinkList):
    def __init__(self) -> None:
        super().__init__()

    def mid_or_upmid(self):
        # 如果是奇数个，返回重点，如果是偶数个，返回上中点
        if self.head == None or self.head.next == None or self.head.next.next == None:
            return self.head
        
        # 此时链表有3个或3个以上的节点
        slow = self.head.next
        fast = self.head.next.next

        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def mid_or_downmid(self):
        # 如果是奇数个，返回重点，如果是偶数个，返回上中点
        if self.head == None or self.head.next == None or self.head.next.next == None:
            return self.head
        
        # 此时链表有3个或3个以上的节点
        slow = self.head.next
        fast = self.head.next

        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def mid_or_upmid_pre(self):
        if self.head == None or self.head.next == None:
            return self.head

        if self.head.next.next != None:
            return self.head.next.next

        

    def mid_or_downmid_pre(self):
        if self.head == None or self.head.next == None:
            return self.head
        if self.head.next.next == None:
            return self.head

        slow = self.head
        fast = self.head.next

        while (fast.next != None and fast.next.next != None):
            slow = slow.next
            fast = fast.next.next
        return slow

        

if __name__ == "__main__":
    l = LinkList()
    l.add(Node(1))
    l.add(Node(3))
    l.add(Node(5))
    l.add(Node(8))
    l.add(Node(9))
    l.add(Node(10))
    # l.add(Node(11))
    l.p()
    print('===========================')
    print(l.mid_or_upmid().value)
    print(l.mid_or_downmid().value)