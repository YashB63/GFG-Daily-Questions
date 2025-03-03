from collections import defaultdict

class Solution:
    def longestPerfectPiece(self, arr, N):
        dc = defaultdict(int)
        l =0
        r = 0
        max_ln, cur_ln = 1, 1
        while r < N:
            if max(dc.keys(), default=0) - min(dc.keys(), default=0) <2:
                cur_ln = sum(dc.values())
                dc[arr[r]]+=1
                r+=1
            else:
                max_ln = max(max_ln, cur_ln)
                cur_ln = 1
                dc[arr[l]]-=1
                if dc[arr[l]] ==0:
                    del dc[arr[l]]
                l+=1
        if max(dc.keys(), default=0) - min(dc.keys(), default=0) <2:
            cur_ln = sum(dc.values())
        max_ln = max(max_ln, cur_ln)
        return max_ln