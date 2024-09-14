class Solution:
	def minJumps(self, arr):
        n=len(arr)
        x=y=jumps=0
        for i in range(n-1):
            y=max(y, i+arr[i])
            if x==i:
               if y==i:
                   return -1
               jumps += 1
               x=y
        return jumps