class Solution:
    #Function to rearrange  the array elements alternately.
    def rearrange(self,arr, n): 

        res = sorted(arr)
        start = 0
        end = n-1
        for i in range(n):
            if i % 2 == 0:
                arr[i] = res[end]
                end-=1
            else:
                arr[i] = res[start]
                start+=1