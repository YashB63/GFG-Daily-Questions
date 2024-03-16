class Solution:
	def countPairs(self, mat1, mat2, n, x):
		
        a=[j for i in mat1 for j in i]
        b=[j for i in mat2 for j in i]
        b=set(b)
        res=0
        for i in a:
            if x-i in b:
                res+=1
        return res