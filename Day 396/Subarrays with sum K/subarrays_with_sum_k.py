class Solution:
    def countSubarrays(self, arr, k):
        c=0
        s=0
        s1={0:1}
        for num in arr:
            s+=num
            if s-k in s1:
                c+=s1[s-k]
            s1[s]=s1.get(s,0)+1
        return c