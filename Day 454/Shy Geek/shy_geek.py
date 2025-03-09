class Solution:
    shop=Shop()
    def __init__(self,shop):
        self.shop=shop
    
    def find(self,n,k):
        def getEqualOrLowerValue(val,l,h):
            ansInd=-1;ans=-1
            while l<=h:
                mid=(l+h)//2
                getVal=self.shop.get(mid)
                if ans<getVal<=val:
                    ansInd=mid
                    ans=getVal
                    l=mid+1
                else:
                    h=mid-1
            return ansInd,ans
        l=0;h=n-1
        amount=k
        count=0
        while amount!=0:
            ansInd,ans=getEqualOrLowerValue(amount,l,h)

            if ansInd!=-1:
                count+=amount//ans
                amount=amount%ans

            else:
                break
            h=ansInd
        return count