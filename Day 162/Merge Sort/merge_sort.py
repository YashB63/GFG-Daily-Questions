class Solution:
    def merge(self,arr, l, m, r): 
        
        vector = [0] * ((r - l ) + 1)
        left , right , index = l , m + 1 ,  0 
        while left <= m and right  <= r:
            if arr[left] <= arr[right]:
                vector[index] = arr[left]
                left +=1
                index +=1
            else:
                vector[index] = arr[right]
                right +=1
                index +=1
        while left <= m:
            vector[index] = arr[left]
            index +=1
            left +=1
        while right <= r:
            vector [index] = arr[right]
            index +=1
            right +=1
        for i in range(len(vector)):
            arr[l + i] = vector[i]
            
    def mergeSort(self,arr, l, r):
       
        if l < r:
            mid = (l + r) // 2
            self.mergeSort(arr , l , mid)
            self.mergeSort(arr , mid+1 , r)
            self.merge(arr , l , mid , r)