class Solution:
    def findPairs(self, arr, n):
        result = []
        ump = {}  
        
        for i in range(n):
            
            ump[arr[i]] = 1

            if ump.get(-arr[i], 0) == 0 or arr[i] == 0:
                ump[arr[i]] = 1
            else:
                result.append(-abs(arr[i]))
                result.append(abs(arr[i]))

        return result