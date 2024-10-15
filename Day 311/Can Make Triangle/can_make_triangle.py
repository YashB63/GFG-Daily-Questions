class Solution:
    def canMakeTriangle(self, arr, n): 
        res = [0]*(n-2)
       
        for i in range(n-2):
            a = arr[i] 
            b = arr[i+1]
            c = arr[i+2]
           
            if a+b>c and b+c>a and c+a>b:
                    res[i] = 1
               
        return res