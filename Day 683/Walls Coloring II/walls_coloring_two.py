class Solution:
    def minCost(self, costs : list[list[int]]) -> int:
        if not costs:
            return 0
        n=len(costs)
        k=len(costs[0])
        if k==1 and n==1:
            return costs[0][0]
        if k<2:
            return -1
        
        dp=[0]*k
        m1=[0,0]
        m2=[0,1]
        for i in range(n):
            temp=[0]*k
            d1=[float('inf'),0]
            d2=[float("inf"),0]
            for j in range(k):
                if j==m1[1]:
                    temp[j]=m2[0]+costs[i][j]
                else:
                    temp[j]=m1[0]+costs[i][j]
                if temp[j]<d1[0]:
                    d2=d1
                    d1=[temp[j],j]
                elif temp[j]<d2[0]:
                    d2=[temp[j],j]
            m1=d1
            m2=d2
            dp=temp
        return m1[0]