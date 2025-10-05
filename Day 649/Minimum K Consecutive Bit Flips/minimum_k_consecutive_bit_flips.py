from collections import deque

class Solution:
    def kBitFlips(self, arr, k):
        n = len(arr)
        res = 0
        flag = 0
        q = deque()

        for i in range(n):
            if i >= k:
                flag ^= q.popleft()

            if flag == 1:
                arr[i] ^= 1

            if arr[i] == 0:
                if i + k > n:
                    return -1
                
                res += 1
                flag ^= 1
                q.append(1)
                
            else:
                q.append(0)

        return res