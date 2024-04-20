class Solution:
    def minPartition(self, N):
        
        notes=[ 1, 2, 5, 10, 20, 50, 100, 200, 500, 2000 ]
        notes.sort(reverse=True)
        ans=[]
        for v in notes:
            if N==0:
                break
            z=N//v
            if z!=0:
                ans.extend([v]*z)
                N-=v*z
        return ans