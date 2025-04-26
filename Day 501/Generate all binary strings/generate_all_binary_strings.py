class Solution:
    def generateBinaryStrings(self, n):
        l1=[]
        fun("",l1,n)
        return sorted(l1)
        
def fun(s1,l1,n):
    if len(s1)==n:
        if '11' not in s1:
            l1.append(s1)
        return 
    fun(s1+'1',l1,n)
    fun(s1+'0',l1,n)