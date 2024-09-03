class Solution:
    def sortBySetBitCount(self, arr, n):
        arr.sort(key=lambda x:bin(x)[2:].count('1'), reverse=True)