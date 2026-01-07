class Solution:
    def countLessEqual(self, arr, x):
        return sum(1 for i in arr if i <= x)