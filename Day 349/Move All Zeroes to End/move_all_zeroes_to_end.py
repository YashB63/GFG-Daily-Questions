class Solution:
	def pushZerosToEnd(self,arr):
        n = len(arr)
        x = 0
        for i in range(n):
            if arr[i] != 0:
                arr[x], arr[i] = arr[i], arr[x]
                
                x += 1
                
        return arr