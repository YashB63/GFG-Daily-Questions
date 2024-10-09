class Solution:
    def strangeSort (self,arr, k):
        l=[]
        for i in range(len(arr)):
            if i==k-1:
                a=arr[i]
            else:
                l.append(arr[i])
        l.sort()
        l.insert(k-1,a)
        for i in range(len(l)):
            arr[i]=l[i]
        return arr