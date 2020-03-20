#coding: utf-8

"""
单链表
"""

class Node(object):
    def __init__(self, value=0):
        self.value = value
        self.next = None

class SingleLinkList:
    head = None
    def add(self, Node):
        if self.head == None:
            self.head = Node
        else:
            t_p = self.head
            while t_p.next != None:
                t_p = t_p.next
            t_p.next = Node    
            

    def p(self):
        t_p = self.head
        while t_p != None:
            print(t_p.value)
            t_p = t_p.next
            

if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(3)
    n3 = Node(5)
    s = SingleLinkList()
    s.add(n1)
    s.add(n2)
    s.add(n3)
    s.p()
