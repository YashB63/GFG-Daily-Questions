class Solution:
    def findNum(self, n : int):
        
        count=0
        num=5
        while True:
            temp=num
            while temp%5==0:
                count+=1
                temp//=5
            if count>=n:
                return num
            num+=5