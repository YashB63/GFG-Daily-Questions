class Solution:
    def countSubarrays(self, arr):
        n = len(arr)
        next_smaller = [n] * n
        stack = []
        
        for i in range(n):
            while stack and arr[i] < arr[stack[-1]]:
                next_smaller[stack.pop()] = i
            stack.append(i)
        
        return sum(next_smaller[i] - i for i in range(n))