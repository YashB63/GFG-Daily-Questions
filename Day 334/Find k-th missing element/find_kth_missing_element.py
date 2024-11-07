class Solution:

    def findKthMissing(self, arr1, arr2, k):
        m=0
        s=set(arr2)
        for i in arr1:
            if i not in s:
                m+=1
                
            if m==k:
                return i
        else:
            return -1
            
        pass