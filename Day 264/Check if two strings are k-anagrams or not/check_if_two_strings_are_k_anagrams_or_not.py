import collections
class Solution:
    def areKAnagrams(self, str1, str2, k):
        cnt1=collections.Counter(str1)
        cnt2=collections.Counter(str2)
        sm=sum((cnt1-cnt2).values()) + sum((cnt2-cnt1).values())
        return len(str1)==len(str2) and sm/2<=k