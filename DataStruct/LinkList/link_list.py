#coding: utf-8

"""
single link List, and some base algorithms
"""

class Node(object):
    def __init__(self, value=0):
        self.value = value
        self.next = None

class SingleLinkedList:
    def __init__(self, head=None) -> None:
        self.head = head

    # insert a element in the front
    def insert(self, x) -> None:
        nex = self.head
        x.next = nex
        self.head = x

    def build_with_list(self, data_list:list) -> None:
        cur = self.head
        for data in data_list:
            if self.head == None:
                self.head = Node(data)
                cur = self.head
                continue
            
            cur.next = Node(data)
            cur = cur.next
    
    # search
    def search(self, val) -> Node:
        cur = self.head
        while cur and cur.value != val:
            cur = cur.next
        return cur

    # delete
    def delete(self, val):
        pre = None
        cur = self.head
        while cur and cur.value != val:
            pre =cur
            cur = cur.next
        
        if cur != None:
            pre.next = cur.next

    def append(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = Node(value)
            

    def print(self):
        cur = self.head
        while cur:
            print("({})".format(cur.value),end="")
            cur = cur.next
            print("->", end="")
        print("|")


class CircularLinkedList:
    def __init__(self) -> None:
        self.h_node = Node(-1)
        # 循环链表，为空的是h_node
        self.h_node.next = self.h_node
        self.tail = None

    def build_with_list(self, data: list):
        cur = self.h_node
        for value in data:
            cur.next = Node(value)
            cur = cur.next
        self.tail = cur
        cur.next = self.h_node

    def print(self):
        cur = self.h_node
        while cur.next != self.h_node:
            cur = cur.next
            print("({})".format(cur.value),end="")
            print("->", end="")
        print("|")



if __name__ == "__main__":
 
    s = SingleLinkedList()

    L = ["ab", "bcc", "cdd", "dee", "eff"]

    s.build_with_list(L)
    s.insert(Node(0))
    s.print()
    print(s.search("bcc"))
    s.delete("dee")
    s.delete("eff")
    s.print()

    s2 = CircularLinkedList()
    s2.build_with_list(L)
    s2.print()
