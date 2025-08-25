class Solution:
    def rearrange(self, arr, x):
        arr.sort(key=lambda a: abs(a - x))