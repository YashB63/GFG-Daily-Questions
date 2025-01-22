class Solution:
    def nearestSmallestTower(self,arr):
        stack=[]
        out = [-1] * len(arr)
        for i, elem in enumerate(arr):
            while stack and arr[stack[-1]] >= elem:
                stack.pop()
            if stack:
                out[i] = stack[-1]
            stack.append(i)
        stack=[]
        for i in range(len(arr) -1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack and (out[i] == -1 or (i -out[i] > stack[-1] -i) or (i - out[i] == stack[-1] - i and arr[stack[-1]] < arr[out[i]])):
                out[i] = stack[-1]
            stack.append(i)
        return out