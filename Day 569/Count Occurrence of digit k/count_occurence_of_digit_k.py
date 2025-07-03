class Solution:
    def count(self, lis, k):
        cnt = 0
        for i in lis:
            if i == k:
                cnt += 1
        return cnt

    def num(self, k, arr):
        cnt = 0
        for e in arr:
            cnt += self.count(list(str(e)), str(k))
        return cnt