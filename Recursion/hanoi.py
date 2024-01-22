import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# from util import time_utils

def hanoi(n, a, b, c):
    if n == 1:
        print("%s -> %s" % (a, c))
    else:
        hanoi(n-1, a, c, b)
        hanoi(1, a, b, c)
        hanoi(n-1, b, a, c)

class Column:
    def __init__(self, name) -> None:
        self.name = name
        self.data = []

def show_columns():
    if len(columns) == 0:
        return
    for c in columns:
        print(c.data, end=" ")
    print()

def hanoi2_move(src:Column, dst:Column):
    print(src.name, "->", dst.name)
    dst.data.insert(0, src.data.pop(0))
    show_columns()


def hanoi2(n, sA, sB, sC):
    if n == 1:
        hanoi2_move(sA, sC)
        return
    hanoi2(n-1, sA, sC, sB)
    hanoi2(1, sA, sB, sC)
    hanoi2(n-1, sB, sA, sC)

global columns
columns = []

"""
this funcion can show the status of the columns
"""
def playHanoi(n):
    # init game
    sA = Column("A")
    sB = Column("B")
    sC = Column("C")
 
    columns.extend([sA, sB, sC])

    for i in range(n):
        sA.data.append(i+1)

    hanoi2(n, sA, sB, sC)
    print(sC.data)
    
        
    
if __name__ == "__main__":
    # time_utils.ti(hanoi)(4,"A", "B", "C")
    hanoi(1, "a", "b", "c")

    playHanoi(5)
