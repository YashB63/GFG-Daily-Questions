class Solution:
    
    def binary_search(self,arr,element):
        low=0
        high= len(arr)-1
        while low<=high:
            mid= (low+high)//2
            
            if arr[mid]==element:
                return mid
            if arr[mid]<element:
                low=mid+1
            else:
                high=mid-1
                
    def isKSortedArray(self, arr, n, k): 
        sortedarr= sorted(arr)
        
        for i in range(n):
            indnew= self.binary_search(sortedarr,arr[i])
            if abs(indnew-i)>k:
                return "No"
        return "Yes"