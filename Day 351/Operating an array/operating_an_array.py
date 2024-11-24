class Solution:
    
    def searchEle(self,arr, x):
        return x in arr

    def insertEle(self,arr, y, yi):
        if 0<=yi<= len(arr):
            arr.insert(yi,y)
    
    def deleteEle(self,arr, z):
        if z in arr:
            arr.remove(z)