'''
@Author: yangxingchen
@Date: 2020-05-07 17:15:21
@LastEditors: yangxingchen
@LastEditTime: 2020-05-07 17:25:40
@Description: 
'''
from bst import *
from BinarySearchTree import *

class Tree:

    """前序遍历的交换
    """
    def invertTree(self, root):
        if root == None:
            return
        # 交换
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        # 中序遍历
        self.invertTree(root.left)
        root.left, root.right = root.right, root.left
        # 因为已经交换了
        self.invertTree(root.left)