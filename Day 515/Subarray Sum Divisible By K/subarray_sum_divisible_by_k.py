class Solution:
    def subCount(self, arr, k):
        dict1={0:1}
        ans=0
        for i in range(len(arr)):
            if i-1>=0:
                arr[i]+=arr[i-1]
            rem = arr[i]%k
            
            if rem in dict1:
                ans+=dict1[rem]
                dict1[rem]+=1
            else:
                dict1[rem]=1
        return ans