class Solution:
    def sort012(self,arr,n):
        
        ones = 0
        zeros = 0
        for i in range(n):
            if arr[i]==0:
                zeros+=1
            elif arr[i]==1:
                ones+=1
        for i in range(n):
            if zeros:
                arr[i]=0
                zeros-=1
            elif ones:
                arr[i]=1
                ones-=1
            else:
                arr[i]=2
