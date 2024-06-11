class Solution:
    def findSwapValues(self,a, n, b, m):
        
        suma = sum(a)
        sumb = sum(b)
        diff = sumb-suma
        
        if diff & 1:
            return -1
            
        diff /= 2
        
        a.sort()
        b.sort()
        
        p1 = 0
        p2 = 0

        while p1 < n and p2 < m:
            diff2 = b[p2] - a[p1]

            if diff2 == diff:
                return 1
            elif diff2 > diff:
                p1 += 1
            else:
                p2 += 1
        
        return -1