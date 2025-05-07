class Solution:
	def UniquePartitions(self, n):
        res = []
        def recur(part,part_sum,max_val):
            if part_sum==n:
                res.append(part[:])
                return
            for i in range(max_val,0,-1): 
                if part_sum+i<=n:
                    part.append(i)
                    recur(part,part_sum+i,i) 
                    part.pop()
        recur([],0,n)
        return res