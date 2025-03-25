class Solution:
    def maxWater(self, arr):
        n=len(arr)
        i,j=0,n-1
        left_max=0
        right_max=0
        total=0
        while i<j:
            if arr[i]>=arr[j]:
                if arr[j]>right_max:
                    right_max=arr[j]
                total+=max(0,right_max-arr[j])
                j-=1
            elif arr[i]<arr[j]:
                if arr[i]>left_max:
                    left_max=arr[i]
                total+=max(0,left_max-arr[i])
                i+=1
            
        return total