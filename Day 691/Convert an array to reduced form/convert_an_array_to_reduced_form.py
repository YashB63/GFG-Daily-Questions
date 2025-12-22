class Solution:
	def convert(self,arr, n):
		v=[]
		for i in range(n):
		    v.append((arr[i],i))
		v.sort()
		for i in range(n):
		    arr[v[i][1]]=i