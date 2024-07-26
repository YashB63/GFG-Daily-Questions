class Solution:
    def maxOnes(self, a, n):
        
        count=0
        for i in range(n):
            if a[i]==1:
                a[i]=-1
                count+=1
            else:
                a[i]=1
        mx=0
        sum=0
        for i in range(n):
            sum+=a[i]
            mx=max(sum,mx)
            if sum<0:
                sum=0
        return mx+count
