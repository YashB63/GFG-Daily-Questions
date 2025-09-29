class Solution:
    def longestSubarray(self, arr):
        n = len(arr)

        nextGreater = [n] * n
        prevGreater = [-1] * n
        st = []

        for i in range(n):
            while st and arr[st[-1]] < arr[i]:
                nextGreater[st.pop()] = i
            st.append(i)
        st.clear()

        for i in range(n - 1, -1, -1):
            while st and arr[st[-1]] < arr[i]:
                prevGreater[st.pop()] = i
            st.append(i)

        maxLength = 0
        for i in range(n):
            windowSize = nextGreater[i] - prevGreater[i] - 1
            if windowSize >= arr[i]:
                maxLength = max(maxLength, windowSize)

        return maxLength