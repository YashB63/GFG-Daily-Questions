from collections import deque

class Solution:
    def __init__(self):
        self.prime=[1 for i in range(10001)]
        self.prime[0] = self.prime[1] = 0
        for i in range(2, int(10001 ** 0.5) + 1):
            if self.prime[i]:
                for j in range(i*i, 10001, i):
                    self.prime[j] = 0
                

    def shortestPath(self,Num1,Num2):
        def generateNumbers(num):
            num = str(num)
            l = []
            for i in range(4):
                for d in "0123456789":
                    if d != num[i]:
                        nv = num[:i] + d + num[i+1:]
                        if 1000 <= int(nv) <= 9999:
                            l.append(int(nv))
            return l
        
        
        q = deque([Num1])
        visit = set([Num1])     
        res = 0
        while q:
            size = len(q)
            for _ in range(size):
                val = q.popleft()
                if val == Num2:
                    return res
                for nv in generateNumbers(val):
                    if self.prime[nv] and nv not in visit:
                        visit.add(nv)
                        q.append(nv)
            res += 1
        return -1