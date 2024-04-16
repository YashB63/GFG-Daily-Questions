class Solution:
    def columnWithMaxZeros(self,arr,N):
        
        m=0
        s=0
        k=0
        for i in range(len(arr)):
            c=0
            for j in range(len(arr)):
                if arr[j][i]==0:
                    c+=1
            if c>m:
                s=k
                m=c
            k+=1
        if m==0:
            return -1
        return s