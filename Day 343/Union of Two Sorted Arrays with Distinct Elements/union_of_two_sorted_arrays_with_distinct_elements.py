class Solution:
    def findUnion(self,a,b):
        a.extend(b)
        myset=set(a)
        mylist=list(myset)
        mylist.sort()
        return mylist