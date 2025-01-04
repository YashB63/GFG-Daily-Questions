class Solution:
    def catchThieves(self, arr, n, k): 
        p = [(i, x) for i,x in enumerate(arr) if x == "P"]
        t = [(i, x) for i,x in enumerate(arr) if x == "T"]
        ans = 0
        while p and t:
            i, x = p[-1]
            j, y = t[-1]
            if abs(j-i) <= k:
                p.pop()
                t.pop()
                ans += 1
            else:
                if j > i:
                    t.pop()
                else:
                    p.pop()
        return ans