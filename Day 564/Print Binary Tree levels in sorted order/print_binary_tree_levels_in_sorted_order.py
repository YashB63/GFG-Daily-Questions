class Solution:
    def binTreeSortedLevels (self,arr, n):
        res = []
        i = 0
        
        ls = 1
        while i < n:
            t = (1 << ls) - 1
            t = min (t, n)
            temp = sorted (arr[i : t])
            
            i = t
            ls += 1
            res.append (temp)
        return res