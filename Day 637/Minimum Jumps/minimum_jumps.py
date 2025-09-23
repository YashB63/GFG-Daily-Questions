class Solution:
    def minJumps(self, arr):
        n = len(arr)

        if arr[0] == 0:
            return -1

        maxReach = 0

        currReach = 0

        jump = 0

        for i in range(n):
            maxReach = max(maxReach, i + arr[i])

            if maxReach >= n - 1:
                return jump + 1
                
            if i == currReach:
                if i == maxReach:
                    return -1

                else:
                    jump += 1
                    currReach = maxReach

        return -1