'''
@Author: yangxingchen
@Date: 2020-04-23 08:30:06
@LastEditors: yangxingchen
@LastEditTime: 2020-05-09 18:14:16
@Description: 
'''

from bst import *

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

    def predecessor(node):
        if not node:
            return None
        # 前驱结点在左子树当中
        p = node.left
        if not p:
            while p.right != None:
                p = p.right
            return p
        # 左子树为空

        while node.parent node == node.parent.left:
            node = node.parent
        # node.parent == null
        # node == parent.right 
        return node.parent  


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

    def hight(self):
        return self.hight_node(self.root)

    def hight2(self):
        return self.hight_node2(self.root)

    def hight_node(self, node):
        if node == None:
            return 0
        return 1 + \
                max(self.hight_node(node.left), self.hight_node(node.right))

    def hight_node2(self, node):
        """层序遍历计算高度

        Arguments:
            node {[type]} -- [description]

        Returns:
            [type] -- [description]
        """
        height = 0
        # 每一层元素的个数
        level_size = 1
        if node == None:
            return height
        q = []
        # 头节点进队列
        q.append(node)
        while len(q) > 0:
            cur_node = q.pop(0)
            level_size -= 1
            
            if cur_node.left:
                q.append(cur_node.left)
            if cur_node.right:
                q.append(cur_node.right)
            # 该层已经遍历完了
            if level_size == 0:
                level_size = len(q)
                height += 1
        return height

    """是否为完全二叉树
    """
    def is_complete_tree(self):
        if self.root == None:
            return False
        
        q = []
        leaf  = False
        # 头节点进队列
        node = self.root
        q.append(node)
        while len(q) > 0:
            cur_node = q.pop(0)
            if leaf and (not cur_node.is_leaf()):
                return False

            if cur_node.left and cur_node.right:
                q.append(cur_node.left)
                q.append(cur_node.right)
            elif not cur_node.left and cur_node.right:
                # 左空右不空
                print("====")
                return False
            else:
                # 结点必须是叶子结点
                leaf = True
                if cur_node.left:
                    q.append(cur_node.left)
        return True

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
    test_data = [7, 4, 9, 2, 5, 8, 11]
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
    print(bt.hight())
    print(bt.hight2())
    print(bt.is_complete_tree())