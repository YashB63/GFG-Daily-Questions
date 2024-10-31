class Solution:
    def alternateSort(self,arr):
        arr.sort() 
        l=[]
        j=0
        h=len(arr)-1
        while j<h:
            l.append (arr[h])
            l.append (arr[j])
            j+=1
            h-=1
        if len(arr)%2!=0:
            l.append (arr[j])
        return l