class Solution:
    def sumOfMatrix(self,N,M,Grid):
        a=[]
        for i in Grid:
            for j in i:
                a.append(j)
        return sum(a)