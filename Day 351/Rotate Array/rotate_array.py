class Solution: 
    def rotateArr(self, arr, d):
        n=len(arr)
        d=d%n
        
        if d==0:
            return arr
        else:
            x=arr[d:n]+arr[:d]
            for i in range(n):
                arr[i]=x[i]