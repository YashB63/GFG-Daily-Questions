class Solution:
    def isPallindrome(self, N):
        binary_representation = bin(N)[2:]
        
        if binary_representation == binary_representation[::-1]:
            return 1
        else:
            return 0