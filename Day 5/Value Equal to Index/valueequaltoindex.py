class Solution:

	def valueEqualToIndex(self,arr, n):
        result = []
        for i in range(n):
            if arr[i] == i+1:
                result.append(i+1)
        return result
