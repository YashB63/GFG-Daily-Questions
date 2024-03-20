class Solution:

	def maxIndexDiff(self,arr,n):
		
        lm=[0]*n
        lm[0]=arr[0]
        for i in range(1,n):
            lm[i]=min(lm[i-1],arr[i])
        max1=-1
        i=j=n-1
        while i>=0 and j>=0:
            if arr[j]>=lm[i]:
                max1=max(max1,j-i)
                i-=1
            else:
                j-=1
        return max1