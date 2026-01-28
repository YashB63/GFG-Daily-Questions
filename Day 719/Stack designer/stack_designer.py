class Solution:
    def _push(self, arr):
        stack = []
        for element in arr:
            stack.append(element)
        return stack

    def _pop(self, stack):
        while stack:
            print(stack[-1], end=" ")
            stack.pop()