'''
@Author: yangxingchen
@Date: 2020-04-23 08:30:06
@LastEditors: yangxingchen
@LastEditTime: 2020-05-06 18:40:57
@Description: 
'''

class Node:
    element = None
    left = None
    right = None
    parent = None

    def __init__(self, element, parent):
        self.element = element
        self.parent = parent

class BinarySearchTree:
    def __init__(self):
        self.size = 0
        self.root = None
    
    def size(self):
        return self.size

    def add(self, element):
        if not element:
            return -1
        # 第一个结点
        if self.root == None:
            self.root = Node(element, None)
            self.size += 1
            return
        
        parent = None
        node = self.root
        while node != None:
            parent = node
            if element > node.element:
                # 大,右移
                node = node.right
            elif element < node.element:
                node = node.left
            else:
                # 相等
                return
        # 父结点，看方向
        if (element >= parent.element):
            parent.right = Node(element, parent)
        else:
            parent.left = Node(element, parent)
        self.size += 1

    def preorder_raversal(self, node):
        if node == None:
            return
        print(node.element)
        self.preorder_raversal(node.left)
        self.preorder_raversal(node.right)

    def midorder_traversal(self, node):
        if node == None:
            return
        self.midorder_traversal(node.left)
        print(node.element)
        self.midorder_traversal(node.right)

    def level_order(self, node):
        """层序遍历

        Arguments:
            node {[type]} -- [description]
        """
        q = []
        if node == None:
            return
        # 头节点进队列
        q.append(node)
        while len(q) > 0:
            cur_node = q.pop(0)
            print(cur_node.element)
            if cur_node.left:
                q.append(cur_node.left)
            if cur_node.right:
                q.append(cur_node.right)

    def __str__(self):
        sb = []
        prifix = []
        self.to_str(self.root, sb, prifix)
        return ''.join(sb)

    def to_str(self, node, str_list, pre_list):
        if node == None:
            return str_list
        str_list.append(''.join(pre_list) + str(node.element))
        str_list.append('\n')
        self.to_str(node.left, str_list, pre_list + ['L---'])
        self.to_str(node.right, str_list, pre_list + ['R---'])
        
        

if __name__ == "__main__":
    bt = BinarySearchTree()
    test_data = [7, 4, 9, 2, 5, 8, 11, 3]
    """
        7
      4      9
    2   5  8    11
       3
    """
    for i in test_data:
        bt.add(i)
    # bt.preorder_raversal(bt.root)
    print("=========")
    # bt.midorder_traversal(bt.root)
    print("=========")
    # bt.level_order(bt.root)
    print(bt)