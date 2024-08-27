class Solution:
    def isPossible(self, N, arr):
        s=''
        m=0
        for i in arr:
            m+=i
            s+=str(i)
        if m%3==0:
            return 1
        else:
            return 0