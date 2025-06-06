class Solution:
    def canRepresentBST(self, arr, N):
        stack = []
        root = float('-inf')

        for value in arr:
            if value < root:
                return 0

            while stack and stack[-1] < value:
                root = stack.pop()

            stack.append(value)

        return 1