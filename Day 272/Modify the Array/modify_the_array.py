class Solution:
    def modifyAndRearrangeArr (self, arr) : 
        last_non_zero_index=0
        for i in range(len(arr)):
            if arr[i]!=0:
                if i+1<len(arr) and arr[i]==arr[i+1]:
                    arr[i]=arr[i]*2 
                    arr[i+1]=0 
                arr[last_non_zero_index], arr[i] = arr[i], arr[last_non_zero_index]
                last_non_zero_index += 1
    
        return arr