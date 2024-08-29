class Solution:
    def pairWithMaxSum(self, arr):
        n = len(arr)
        score = []
        
        for i in range(n-1):
            score.append(arr[i]+arr[i+1])
        return max(score)