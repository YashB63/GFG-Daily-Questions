import numpy as np

class Solution:
    
    def findUnion(self,arr1,arr2,n,m):
        return np.union1d(arr1,arr2)