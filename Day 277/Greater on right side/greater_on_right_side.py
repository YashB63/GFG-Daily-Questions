class Solution:
	def nextGreatest(self,arr):
		max=-1
        for i in range(len(arr) - 1, -1, -1):
            current = arr[i]
            arr[i] = max
            if current > max:
                max = current

        return arr