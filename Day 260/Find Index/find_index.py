class Solution:
    def findIndex (self,arr, key ):
        l=[]
        ll=[-1,-1]
        if key not in arr:
            return ll
        l.append(arr.index(key))
        for i in range(len(arr)-1,-1,-1):
            if arr[i]==key:
                l.append(i)
                break
        return l