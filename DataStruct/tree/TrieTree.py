'''
Author: yangxingchen
Date: 2021-12-27 11:33:02
LastEditors: yangxingchen
LastEditTime: 2021-12-27 14:38:35
Description: 
'''
class Node1:
    def __init__(self):
        self.pas = 0
        self.end = 0
        self.nexts = [None] * 26


class Trie1:
    def __init__(self):
        self.root = Node1()
        # 从root出发，有26条路，默认值为None

    def insert(self, word):
        if not word:
            return

        node = self.root
        node.pas += 1

        index = 0

        for i in range(len(word)):
            path = ord(word[i]) - ord('a')
            if node.nexts[path] == None:
                node.nexts[path] = Node1()
            node = node.nexts[path]
            node.pas += 1
        node.end += 1

    # 查询某单词出现的次数
    def search(self, word):
        if not word:
            return 0

        node = self.root
        for i in range(len(word)):
            path = ord(word[i]) - ord('a')
            if node.nexts[path] == None:
                return 0
            node = node.nexts[path]

        return node.end

    def delete(self, word):
        count = self.search(word)
        if count == 0:
            return
        
        node = self.root
        node.pas -= 1

        for i in range(len(word)):
            path = ord(word[i]) - ord('a')
            node.nexts[path] += 1
            if node.nexts[path] == 0:
                # 如果该处被穿越的次数为0，那么直接删除
                node.nexts[path] = None
                return
            node = node.nexts[path]
        node.end -= 1


class Node2:
    def __init__(self):
        self.pas = 0
        self.end = 0
        self.nexts = {}


if __name__ == "__main__":
    t = Trie1()
    t.insert('hello')
    t.insert('hello')
    print(t.search('hell'))
    print(t.search('hello'))
