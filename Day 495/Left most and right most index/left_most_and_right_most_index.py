class Solution:
    def indexes(self, v, x):
        num1=-1
        num2=-1
        for i in range(len(v)):
            if v[i]!=x:
                continue
            if num1==-1:
                num1=i
            num2=i
            
        return num1,num2