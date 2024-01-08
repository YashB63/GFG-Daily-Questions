class Solution:
    def singleElement(self, arr, N):
        
        x = {}
        for i in arr:
            x[i] = x.get(i, 0) + 1
        for a,b in x.items():
            if b == 1:
                return a