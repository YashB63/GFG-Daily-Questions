class Solution:
    def maxValue(self, arr):
        n = len(arr)  
        a = []
        b = []

        for i in range(n):
            a.append(arr[i] + i)
            b.append(arr[i] - i)

        max_a = max(a)
        min_a = min(a)
        ans1 = max_a - min_a

        max_b = max(b)
        min_b = min(b)
        ans2 = max_b - min_b

        return max(ans1, ans2)