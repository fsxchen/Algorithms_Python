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
