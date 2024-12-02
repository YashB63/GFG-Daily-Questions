def circularSubarraySum(arr):
    def kadane():
        ans=-math.inf
        summ=0
        for i in arr:
            summ+=i
            ans=max(ans,summ)
            if summ<0:
                summ=0
        
        return ans

    def findMiniSum():
        ans=math.inf
        summ=0
        for i in arr:
            summ+=i
            ans=min(ans,summ)
            if summ>0:
                summ=0
        
        return ans

    ans1=kadane()
    ans2=sum(arr)-findMiniSum()

    return max(ans1,ans2)