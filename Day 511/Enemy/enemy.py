from typing import List

class Solution:
    def largestArea(self,n:int,m:int,k:int, enemy : List[List[int]]) -> int:
        if(len(enemy) == 0):
            return n*m
        if(k == n):
            return 0
       
        rowarr = []
        colarr = []
        for itm in enemy:
            rowarr.append(itm[0])
            colarr.append(itm[1])
            
        rowarr.sort()
        colarr.sort()
        rowarr.append(n+1)
        colarr.append(m+1)
        st = 0
        maxi = 0
        for i in range(len(rowarr)):
            maxi = max(maxi,rowarr[i]-st-1)
            st = rowarr[i]
        
        st = 0
        maxcol = 0
        for i in range(len(colarr)):
            maxcol = max(maxcol,colarr[i]-st-1)
            st = colarr[i]
            
            
        return maxi*maxcol