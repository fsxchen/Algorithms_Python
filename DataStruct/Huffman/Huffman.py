"""霍夫曼编码
"""

class HafNode:
    weight = 0
    parent = None
    lch = None
    rch = None

    def __init__(self, w):
        self.weight = w

    def __gt__(self, other):
        return self.weight > other.weight
    
    def __lt__(self, other):
        return self.weight < other.weight

def create_huffman_tree(l):
    """完成初始化的工作
    
    Arguments:
        l {[type]} -- [description]
    """
    haf_tree = [None] * (2*len(l))
    for i in range(len(l)):
        # 不用0index
        haf_tree[i + 1] = HafNode(l[i])
    return haf_tree

def get_number_of_haffman(haffman_tree):
    n = 0
    for node in haffman_tree:
        if node != None and node.parent == None:
            n += 1
    return n

def get_min_two_from_haffman(haffman_tree):

    min1, min2 = None, None
    for i in range(len(haffman_tree)):
        if haffman_tree[i] != None and haffman_tree[i].parent == None:
            if min1 == None:
                min1 = i
                continue
            if haffman_tree[i] < haffman_tree[min1]:
                min2 = min1
                min1 = i
                continue
            if min2 == None or haffman_tree[i] < haffman_tree[min2]:
                min2 = i

            continue
            
    return min1, min2

def merge(haffman_tree):
    """
    处理n-1 个结点
    """
    for i in range(1, len(haffman_tree)//2):
        print(get_number_of_haffman(haffman_tree))
        min1, min2 = (get_min_two_from_haffman(haf_tree))
        newNode = HafNode(haffman_tree[min1].weight + haffman_tree[min2].weight)
        print(newNode)
        newNode.lch = haffman_tree[min1]
        newNode.rch = haffman_tree[min2]
        haffman_tree[min1].parent = newNode
        haffman_tree[min2].parent = newNode
        haffman_tree[len(haffman_tree)//2 + i] = newNode
    print(haffman_tree)
    print("============")

if __name__ == "__main__":
    test = [7, 19, 2, 6, 32, 3, 21, 10]

    
    # 构造森林全是树
    haf_tree = create_huffman_tree(test)
    merge(haf_tree)

    for i in haf_tree:
        if i == None:
            continue;
        print(i.weight)

    # 选择两小添新树
    
    