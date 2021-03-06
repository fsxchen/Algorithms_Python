#coding:utf-8
"""
反转单链表,
如果有环，则会出现问题
"""

class Node(object):
    def __init__(self, v=0):
        self.value = v
        self.next = None    

class LinkList(object):
    def __init__(self):
        self.head = None

    def add(self, Node):
        t_p = self.head
        if not t_p:
            self.head = Node
            return
        while t_p.next != None:
            t_p = t_p.next
        t_p.next = Node
            
    def p(self):
        """
        顺序打印链表
        """
        t_p = self.head
        while t_p != None:
            print(t_p.value,)
            t_p = t_p.next

    def reverse(self):
        """只要能保证在每次循环的时候
        before: n1 ---> n2 ---> n3 ----> n4
        第一次: n1 ---> none n2 --- > n3 ---> n4
        第二次: n2 ---> n1 ---> none n3 ----> n4
        第三次: n3 ---> n2 ---> n1 ---> none  n4
        ...
        分析：
            1、保存下个指针
            2、将当前指针指向上级指针, 初始状态为None
            3、保存当前指针，为pre
            4、跳转到下一个指针

        """
        # frist move pointer, then reverse
        cur = self.head
        pre = None

        if not cur:
            return
        
        while cur.next:
            next = cur.next
            cur.next = pre
            pre = cur 
            cur = next
        
        cur.next = pre
        self.head = cur 


if __name__ == "__main__":
    ll = LinkList()
    for i in range(9):
        ll.add(Node(i))
    ll.p()
    ll.reverse()
    print("reverse")
    ll.p()
