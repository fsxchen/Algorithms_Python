'''
Author: yangxingchen
Date: 2021-12-23 14:03:48
LastEditors: yangxingchen
LastEditTime: 2021-12-23 15:27:45
Description: 
'''

class HeapList:
    def __init__(self):
        self._heap = [None] * 100
        self.size = 0
        self.limit = 100

    def heap_insert(self, i):
        # 注意这里，当i等于0的时候
        while i > 0 and self._heap[i] > self._heap[(i - 1) // 2]:       # 如果比根节点的数字大
            self._heap[i], self._heap[(i-1)//2] = self._heap[(i-1)//2], self._heap[i]
            i = (i -1) //2
    
    def heapify(self, index):
        """
        堆性质维护,方法：从index位置不断往下看，如果我的孩子都比我大，或者已经没有孩子了。就停止。
        如果某个孩子比我大。那么就和该孩子进行交换。
        """
        left = index * 2 + 1
        
        while left < self.size:             # 此时，有孩子
            # 谁大，给largest, 如果有右孩子，并且右边的孩子比左边的大
            largest = left + 1 if (left + 1 < self.size) and self._heap[left + 1] > self._heap[left] else left
            print(largest, left, index, '...')
            print(self._heap[:10])
            print(self._heap[largest], self._heap[index], 'ooooooo')
            largest = largest if self._heap[largest] > self._heap[index] else index

            if largest == index:
                break
            
            self._heap[largest], self._heap[index] = self._heap[index], self._heap[largest]
            index = largest
            left = index * 2 + 1

    def heapify2(self, index):
        """
        递归版本实现
        """
        if index >= self.size:
            return
        left = index * 2 + 1

        if left >= self.size:
            return
        right = left + 1

        largest = left if right < self.size or self._heap[left] > self._heap[right]  \
                        else right
        
        largest = index if self._heap[index] > self._heap[largest] else largest
        if largest == index:
            return
        else:
            self._heap[index], self._heap[largest] = self._heap[largest], self._heap[index]
            self.heapify2(largest)

    def push(self, value):
        if self.size == self.limit:
            raise "heap is full"
        self._heap[self.size] = value
        self.heap_insert(self.size)
        self.size += 1

    def pop(self):
        """
        返回一个最大值，并删除
        """
        ans = self._heap[0]
        self.size -= 1
        self._heap[0] = self._heap[self.size]
        self.heapify2(0)

def heap_sort(A):
    """利用堆结构实现堆排序

    Args:
        A ([type]): [list]
    """
    n = len(A)
    if n < 2:
        return
    
    heap = HeapList()
    for i in range(n):
        heap.heap_insert(i)
    
if __name__ == "__main__":
    hl = HeapList()
    hl.push(9)
    hl.push(6)
    hl.push(5)
    hl.push(1)
    hl.push(9)
    hl.push(12)

    print(hl._heap)
    print(hl.pop())
    print(hl._heap)
