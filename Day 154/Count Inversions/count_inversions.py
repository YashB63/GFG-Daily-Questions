class Solution:
    
    def inversionCount(self, arr, n):
        
        low = 0
        high = n - 1
        return self.mergeSort(arr, low, high)
    
    def mergeSort(self, arr, low, high):
        if low >= high:
            return 0
        mid = (low+high)//2
        a = self.mergeSort(arr, low, mid)
        b = self.mergeSort(arr, mid+1, high)
        
        
        tmp = self.merge(arr, low, mid, high)
        
        
        return a+b+tmp
    
    def merge(self, arr, low, mid, high):
        
        i = 0
        j = 0
        k = low
        left = arr[low:mid+1]
        right = arr[mid+1:high+1]
        tmp = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i+=1
                k+=1
            else:
                tmp += len(left) - i
                arr[k] = right[j]
                j += 1
                k += 1
        while i < len(left):
            arr[k] = left[i]
            k += 1
            i += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
        return tmp