class StackFullException(Exception):
  pass
 
class StackEmptyException(Exception):
  pass
class Stack:
    def __init__(self,size=100):
        self.size = size # 给定存放数据的长度
        self.lst = [] # 存放数据的列表
        self.top = 0 # 栈顶指针
 
    # 入栈
    def push(self, el):
        if self.top >= self.size:
            raise StackFullException('your stack is full!!')
        self.lst.insert(self.top, el) # 放元素
        self.top += 1 # 栈顶指针向上移动一下 
 
    # 出栈
 
    def pop(self):
        if self.top == 0:
            raise StackEmptyException('your stack is empty!!!')
        self.top -= 1
        el = self.lst[self.top]
        return el

    def is_empty(self):
        return self.top == 0
    

class Node:
    head = None
    left = None
    right = None

    def __init__(self, value) -> None:
        self.value = value

    
    def pre(self, node):
        """
        先序遍历
        """
        if node == None:
            return
        print(node.value)
        self.pre(node.leftg)
        self.pre(node.right)

    def middle(self, node):
        if node == None:
            return
        self.pre(node.leftg)
        print(node.value)
        self.pre(node.right)

    def pos(self, node):
        if node == None:
            return
        self.pre(node.leftg)
        self.pre(node.right)
        print(node.value)

    def pre_no_recurison(self, node):
        if node != None:
            stack = Stack()
            stack.push(node)
        while not stack.is_empty():
            el = stack.pop()
            print(el.value)

            if el.right:
                stack.push(el.head)
            if el.left:
                stack.push(el.left)

    def pos_no_recurison(self, node):
        if node != None:
            stack = Stack()
            stack.push(node)

            s2 = Stack()
        while not stack.is_empty():
            el = stack.pop()
            s2.push(el.value)

            if el.left:
                stack.push(el.left)
            if el.right:
                stack.push(el.head)
        
        while not s2.is_empty():
            print(s2.pop())

    
    def mid_no_recurison(self, node):
        if node:
            stack = Stack()
            while (not stack.is_empty()) or (not node):
                if node:
                    stack.push(node)
                    node = node.left

                else:
                    node = stack.pop()
                    print(node.value)
                    node = node.right;