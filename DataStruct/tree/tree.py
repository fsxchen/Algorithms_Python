'''
Author: yangxingchen
Date: 2023-10-28 17:54:46
LastEditors: yangxingchen
LastEditTime: 2023-10-28 18:08:38
Description: 
'''

# for a binary tree, the node like this

class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.value = val
        self.left = left
        self.right = right

class BinTree:
    def __init__(self, root) -> None:
        self.root = root

    def search(self, value, node:Node):
        pass

    def in_order(self, node:Node):
        if node == None:
            return
        
        if node == None:
            return
        
        self.in_order(node.left)
        print(node.value)
        self.in_order(node.right)



def main():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3, node1)
    node4 = Node(4, node2)
    root = Node(5, node3, node4)
    bt = BinTree(root)
    bt.in_order(bt.root)

if __name__ == "__main__":
    main()

