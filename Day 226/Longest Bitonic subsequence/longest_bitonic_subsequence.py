class Solution:
    def LongestBitonicSequence(self, n : int, nums : List[int]) -> int:
        
        n=len(nums)
        dp1=[1 for _ in range(n)]
        dp2=[1 for _ in range(n)]
        maxlen=1
        for i in range(n):
            for j in range(0,i):
                if(nums[i]>nums[j]):
                    dp1[i]=max(dp1[i],1+dp1[j])
        for i in range(n-1,-1,-1):
            for j in range(n-1,i,-1):
                if(nums[i]>nums[j]):
                    dp2[i]=max(dp2[i],1+dp2[j])    
        maxi=0
        for i in range(n):
            if dp1[i]==1 or dp2[i]==1:
                continue
            dp2[i]+=dp1[i]-1
            maxi=max(maxi,dp2[i])
        return maxi