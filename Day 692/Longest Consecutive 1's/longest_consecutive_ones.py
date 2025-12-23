class Solution:
    def maxConsecutiveOnes(self, N):
        return max(map(len,bin(N)[2:].split('0')))