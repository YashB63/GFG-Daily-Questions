class Solution:
    def nextPermutation(self, arr):
        k=len(arr)-2
        pivort=-1
        index=-1
        me=len(arr)-1 
        for i in range(k,-1,-1):
            if arr[i]<arr[i+1]:
                pivort=arr[i]
                index=i
                break
        if pivort ==-1:
            return arr.reverse()
        else:
            while index<=me:
                if arr[index]<arr[me]:
                    arr[index],arr[me]=arr[me],arr[index]
                    break
                else:
                    me-=1
        me=len(arr)-1 
        index=index+1
        while index<=me:
            arr[index],arr[me]=arr[me],arr[index]
            index+=1
            me-=1
        return arr   