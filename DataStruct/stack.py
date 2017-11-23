#!/usr/bin/env python
#coding:utf-8


class stack(list):
    def top(self):
        return self[-1]
    def push(self, v):
        self.append(v)
    def is_empty(self):
        return True if len(self)== 0 else False
    
s = "9+(3-1)*3+4/2"

fuhao = {"+": 1, "-": 1, "*": 2, "/": 2, "(": 0, ")": 3}

s1 = stack()
s2 = stack()

for i in s:
    if i not in fuhao.keys():
        s1.push(i)
    else:
        if i == "(":
            s2.push(i)
        elif i == ")":
            while 1:
                si = s2.pop()
                if si == "(":
                    break
                else:
                    s1.push(si)
        else:
            if s2.is_empty():
                s2.push(i)
            else:
                while 1: 
                    if s2.is_empty():
                        s2.push(i)
                        break
                    else:
                        if fuhao[i] >= fuhao[s2.top()]:
                            s2.push(i)
                            break
                        else:
                            s1.push(s2.pop())
    print(s2)
    print("...")

while s2.is_empty() == False:
    s1.push(s2.pop())

# jie ni bo lan
print("s1:", s1)

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
s3 = stack()
for i in s1:
    if i not in fuhao.keys():
        s3.push(i)
    else:
        a = s3.pop()
        b = s3.pop()
        s3.push(docal(a,b, i))



print(s2)
print(s3)
