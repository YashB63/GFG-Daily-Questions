class Solution:
    
    def binSearch(self,arr,x):
        lo, hi = 0, len(arr)-1
        while lo<=hi:
            mid = (lo+hi)//2
            if arr[mid]<x:
                lo = mid+1
            else:
                hi=mid-1
        return lo
        
	def constructLowerArray(self,arr):
		
        sortedArr = sorted(arr)
        li=[]
        
        for i in range(len(arr)):
            x = self.binSearch(sortedArr,arr[i])
            li.append(x)
            sortedArr.pop(x)
        
        return li