class Solution:
    def min_sprinklers(self, gallery, n):
        
        intervals = sorted([(i-g, i+g) for i,g in enumerate(gallery) if g != -1], reverse = True)
        reachable, best, res = 0, 0, 0
       
        while reachable < n:
            if intervals and intervals[-1][0] <= reachable:
               s, e = intervals.pop()
               best = max(best, e+1)
            
            elif best > reachable:
                reachable = best
                res += 1
            else:
                return -1
        
        return res