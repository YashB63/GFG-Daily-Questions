class Solution:
    
    def activitySelection(self,n,start,end):
        
        start, end = list(zip(*[(s, e) for e, s in sorted(zip(end, start))]))

        result = 0
        last = 0
        for i in range(n):
            if i == 0 or start[i] > end[last]:
                result += 1
                last = i

        return result