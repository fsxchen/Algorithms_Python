'''
@Author: yangxingchen
@Date: 2020-05-07 17:15:29
@LastEditors: yangxingchen
@LastEditTime: 2020-05-07 17:16:15
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
    
    def is_leaf(self):
        return self.right == None and self.left == None
