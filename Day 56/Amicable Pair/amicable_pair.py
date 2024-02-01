class Solution:
    def isAmicable(self, A , B):
        
        x = list()
        y = list()
        
        for i in range(1, A-1, 1):
            if A%i == 0:
                x.append(i)
                
        for i in range(1, B-1, 1):
            if B%i == 0:
                y.append(i)
                
        if sum(x) == B and sum(y) == A:
            return 1
        else:
            return 0