class Solution:
    def isRotated(self,str1,str2):
        return 1 if str1[2:]+str1[:2] == str2 or str1[-2:]+str1[:-2] == str2 else 0
