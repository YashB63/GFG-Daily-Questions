class Solution:
    def segregate0and1(self, arr, n):
        
        c=0
        for i in range(n):
            if arr[i]==0:
                c+=1
        for i in range(0,c):
            arr[i]=0
        for i in range(c,n):
            arr[i]=1
        for i in range(n):
            return arr[i]