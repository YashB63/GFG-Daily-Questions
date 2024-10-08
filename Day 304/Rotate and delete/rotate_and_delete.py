class Solution:
    
    def rotate(self,arr):
        last  = arr.pop()
        arr.insert(0,last)
        
    def rotateDelete(self,  arr):
        for i in range(1,(len(arr)//2)+1):
            self.rotate(arr) 
            n = len(arr)
            del arr[n-i]
        return arr[0]