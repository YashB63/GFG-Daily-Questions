class Solution:
    def countSubArrayProductLessThanK(self, a, n, k):
        winStart=0
        winProd=1
        subArrayCnt=0
        for winEnd in range(len(a)):
            winProd=winProd*a[winEnd]
            while(winProd>=k and (winStart<=winEnd)):
                winProd=winProd/a[winStart]
                winStart+=1
            winSize=winEnd-winStart+1
            subArrayCnt+=winSize
            
        return subArrayCnt