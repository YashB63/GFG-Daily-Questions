from typing import List

class Solution:
    def finLength(self, N : int, color : List[int], radius : List[int]) -> int:
        stack = []
        for i in range(N):
            if not stack:
                stack.append([color[i], radius[i]])
            else:
                if stack[-1][0] == color[i] and stack[-1][1] == radius[i]:
                    stack.pop()
                else:
                    stack.append([color[i], radius[i]])
        return len(stack)