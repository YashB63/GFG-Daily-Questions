class Solution:
    def evaluate(self, arr):
        s = []
        for i in arr:
            if i in "+-*/":
                b, a = s.pop(), s.pop()
                if i == "+": s.append(a + b)
                elif i == "-": s.append(a - b)
                elif i == "*": s.append(a * b)
                else: s.append(int(a / b))
            else:
                s.append(int(i))
        return s[0]