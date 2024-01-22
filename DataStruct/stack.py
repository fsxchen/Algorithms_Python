#!/usr/bin/env python
#coding:utf-8

"""
堆的典型：波兰/匿波兰表达式的计算
"""

"""
中缀表达式：A+B*(C-D)-E*F
前缀表达式：波兰式
    由相应的语法树的前序遍历的结果得到的,如：
    - + A * B - C D * E F
    由前序表达式计算表达式结果的方法
    如果扫描到操作数，则压进S2，如果扫描到操作符，则从S2弹出两个操作数进行相应的操作，并将结果压进S2(S2的个数出2个进1个),

    当扫描结束后，S2的栈顶就是表达式结果。

后缀表达式：逆波兰式
"""

class stack(object):
    def __init__(self):
        self._stack = []
    """
    使用list构建堆
    """
    def top(self):
        """读取栈顶元素
        Returns:
            [type] -- [description]
        """
        return self._stack[-1]

    def push(self, v):
        self._stack.append(v)

    def pop(self):
        return self._stack.pop()

    def is_empty(self):
        return True if len(self._stack)== 0 else False

    def __getitem__(self, v):
        return self._stack[v]

    def p(self):
        """打印
        """
        for i in self._stack:
            print(i, end="|")
        print()
# 中缀表达式
s = "9+(3-1)*3+4/2"

fuhao = {"+": 1, "-": 1, "*": 2, "/": 2, "(": 0, ")": 0}

def mid2pre(mid_str):
    """中缀表达式转前缀表达式
    
    Arguments:
        mid_str {[type]} -- [中缀表达式]
        方法：1、从右到左遍历字符串
                遇到操作数，
                    压栈进入s1
                遇到操作符
                    如果栈为空或者栈顶为），直接压入s2
                    if 优先级比>= 栈顶，直接压入s2
                    else 出栈，后压入s1，继续上一步
                
                遇到括号：
                    如果是)直接压入s2
                    如果是(, 则弹出s2的栈顶, 并押入到s1，直到遇到),并丢弃括号
    """
    s1 = stack()
    s2 = stack()
    for s in reversed(mid_str):
        # 如果是数字，直接push到s1
        if not s in fuhao.keys():
            s1.push(s)
            continue
        # 符号，如果s2 为空
        if s2.is_empty():
            s2.push(s)
            continue
        # 遇到右括号
        if s == ")":
            s2.push(s)
            continue

        if s == "(":
            while 1:
                top = s2.pop()
                if top == ")":
                    break
                s1.push(top)
            continue
        while not s2.is_empty() and fuhao[s] < fuhao[s2.top()]:
            s1.push(s2.pop())
        s2.push(s)
    
    while not s2.is_empty():
        s1.push(s2.pop())
        
    tmp_s = []
    while not s1.is_empty():
        tmp_s.append(s1.pop())

    return "".join(tmp_s)


def docal(a, b, f):
    a = float(a)
    b = float(b)
    if f == "+":
        return a+ b
    if f == "-":
        return b-a
    if f == "*":
        return a*b
    if f == "/":
        return b/a
        

def calcu(pre_exp):
    """前缀表达式求值
    
    Arguments:
        pre_exp {[type]} -- [description]
    """
    tmp_stack = stack()
    for s in reversed(pre_exp):
        # 操作数
        if s not in fuhao.keys():
            tmp_stack.push(s)
            continue
        
        # 符号
        a = tmp_stack.pop()
        b = tmp_stack.pop()
        
        tmp_stack.push(docal(b, a, s))

    tmp_stack.p()



if __name__ == "__main__":
    print(s)
    qianzhui = mid2pre(s)
    calcu(qianzhui)
    # print(s2)
    # print(s3)
