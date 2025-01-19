class Solution:
    def lookandsay(self, n):
        if n == 1:
            return "1"
            
        prev = self.lookandsay(n-1)
        res = ''
        count = 1
        
        for i in range(len(prev)):
            if i+1<len(prev) and prev[i] == prev[i+1]:
                count += 1
            else:
                res += str(count) + prev[i]
                count = 1
        
        return res