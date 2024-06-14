class Solution:
	def subsetSums(self, a, n):
		
        ans =[]
        for i in range (1, (1<<n)+1):
            sum = 0
            for j in range(n):
                if (1<<j)&i:
                    sum+=a[j]
            ans.append(sum)
        return ans
