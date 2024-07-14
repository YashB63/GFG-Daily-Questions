class Solution:
    def search(self,arr,key):
        index = 0
        if key not in arr:
            return -1
        
        else:
            index = arr.index(key)
        
        return index