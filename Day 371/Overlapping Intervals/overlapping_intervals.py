class Solution:
	def mergeOverlap(self, arr):
        arr.sort(key= lambda x:x[0])
        ans=[]
        ans.append(arr[0])
        for i in range(1,len(arr)):
            if arr[i][0]<=ans[-1][1]:
                ans[-1][1]=max(ans[-1][1],arr[i][1])
            else:
                ans.append(arr[i])
        return ans
