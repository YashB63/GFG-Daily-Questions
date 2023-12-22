class Solution:
    def rearrange(self,arr, n):
        x = []
        y = []
        
        for i in range(n):
            if arr[i] >= 0:
                x.append(arr[i])
            else:
                y.append(arr[i])
                
        res = []
        
        while(x and y):
            z = x.pop(0)
            res.append(z)
            w = y.pop(0)
            res.append(w)
        
        if x:
            for i in x:
                res.append(i)
        else:
            for i in y:
                res.append(i)
        
        for i in range(n):
            arr[i] = res[i]