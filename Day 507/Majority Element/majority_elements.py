from collections import Counter

class Solution:
    def majorityElement(self, arr):
        cnt=Counter(arr)
        n=len(arr)
        for i in arr:
            if cnt[i]>(n//2):
                return i
        return -1