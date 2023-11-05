#coding: utf-8

"""
single link List, and some base algorithms
"""

class Node(object):
    def __init__(self, value=0):
        self.value = value
        self.next = None

class SingleLinkList:
    def __init__(self) -> None:
        self.head = None

    def append(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            t_p = self.head
            while t_p.next != None:
                t_p = t_p.next
            t_p.next = Node(value)
            

    def p(self):
        t_p = self.head
        while t_p != None:
            print("({})".format(t_p.value),end="")
            t_p = t_p.next
            if t_p != None:
                print("->", end="")
        print()

if __name__ == "__main__":
 
    s = SingleLinkList()

    L = ["ab", "bcc", "cdd", "dee", "eff"]

    for i in L:
        s.append(i)

    s.p()
