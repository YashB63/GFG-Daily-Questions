class Solution: 
    
    def selectionSort(self, arr,n):
       
        for i in range(0,n-1):
            imin=i
            for j in range(i+1,n):
                if arr[imin]>arr[j]:
                    imin=j
            temp=arr[imin]
            arr[imin]=arr[i]
            arr[i]=temp