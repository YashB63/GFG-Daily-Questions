class Solution:
    def count_pairs(self, arr, s):
        c=0
        for i,j in arr:
            if i in s and j in s:
                c+=1
        return c