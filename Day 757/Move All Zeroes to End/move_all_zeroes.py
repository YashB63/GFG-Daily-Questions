class Solution:
	def pushZerosToEnd(self, arr):
        n = len(arr)
        j = 0
       
        for i in range(n):
            if arr[i] != 0:
                arr[j], arr[i] = arr[i], arr[j]
                j += 1
                
        return arr