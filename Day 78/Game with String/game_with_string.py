class Solution:
    def minValue(self, s, k):
       
        d = {}
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        while k>0:
            mx = max(d.values())
            for key, val in d.items():
                if val == mx:
                    d[key] -= 1
                    break
                
            k -= 1
            
        res = 0
        for key, val in d.items():
            res += val**2
        return res