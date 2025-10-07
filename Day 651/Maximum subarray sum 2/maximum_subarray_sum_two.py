from collections import deque

class Solution:
    def maxSubarrSum(self, arr, a, b):
        n = len(arr)

        for i in range(1, n):
            arr[i] += arr[i - 1]
        maxi = arr[a - 1]

        dq = deque()
        dq.append(0)

        for i in range(a, n):
            if i - b - 1 >= 0:
                if dq and dq[0] == arr[i - b - 1]:
                    dq.popleft()
            elif i - b == 0:
                if dq and dq[0] == 0:
                    dq.popleft()

            while dq and dq[-1] > arr[i - a]:
                dq.pop()

            dq.append(arr[i - a])

            maxi = max(maxi, arr[i] - dq[0])

        return maxi
