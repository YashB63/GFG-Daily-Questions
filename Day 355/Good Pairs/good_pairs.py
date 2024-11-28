class Solution:
    def solve(self, arr : list, n : int):
        arr.sort()
        c=0
        res=0
        for i in range(1,n):
            if arr[i]!=arr[i-1]:
                res+=i
                c=i
            else:
                res+=c
        return res