"""
字符串全排列
"""

def quanpailie(s, l):
    if len(s) == 1:
        l.append(s[0])
        l.append(" ")
        return l
    else:
        print(s)
        print(l)
        return quanpailie(s[1:], l)

if __name__ == "__main__":
    s = "he"
    l = []
    print(quanpailie(s, l))