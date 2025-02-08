class Solution:

	def removals(self,ar, n, k):
        ar.sort()
        i, j = 0, 0
        w = 0
        while(j < n):
            while(i <= j and i < n and j < n):
                if(ar[j]-ar[i] <= k):
                    w = max(w, j-i+1)
                    j += 1
                else:
                    i+=1
            j += 1
        return n-w