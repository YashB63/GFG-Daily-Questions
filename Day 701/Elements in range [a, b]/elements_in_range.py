from bisect import bisect_left, bisect_right

class Solution:
    def cntInRange(self, arr, queries):
        l=[]

        arr.sort()

        for a,b in queries:

            l.append(bisect_right(arr,b)-bisect_left(arr,a))

        return l