class Solution: 
    def firstAndLast(self, x, arr): 
        if x not in arr:
            return [-1]
        res = [0 , 0]
        for i in range(len(arr)):
            if arr[i] == x:
                res[0] = i
                break
        for j in range(len(arr)-1,0,-1):
            if arr[j] == x:
                res[1] = j
                break
        return res