class Solution:
	def countTriplet(self, arr, n):
		
        arr.sort()
        x = set(arr)
        y = 0
        
        for i in range(len(arr) - 2):
            for j in range(i + 1, len(arr) - 1):
                if arr[i] + arr[j] in x:
                    y += 1
        return y