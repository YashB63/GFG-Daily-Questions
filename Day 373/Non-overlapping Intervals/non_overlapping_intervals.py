class Solution:
    def minRemoval(self, intervals):
        n=len(intervals)
        intervals.sort(key=lambda x:x[1])
        ans=0
        val=intervals[0][1]
        for i in range(1,n):
            if intervals[i][0]<val:
                ans+=1
            else:
                val=intervals[i][1]
        return ans