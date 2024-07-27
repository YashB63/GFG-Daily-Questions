class Solution:
    def findMaxProduct(self, arr):
        mod,ans,np,info,maxi,pinfo,nc=1000000007,1,1,False,-10000,False,0
        for i in arr:
            if(i > 0):
                 pinfo=True;
                 ans=(ans*i)%mod
            elif(i==0):
                 info=True
            else:
                 nc=nc+1;
                 np=(np*i)
                 if(maxi < i):
                      maxi=i;
        if(pinfo==False and nc==1):
            if(info):
                ans=0
            else:
                ans=np
        elif(pinfo==False and nc==0):
            ans=0;
        elif(np > 0):
            ans=(ans*(np%mod))%mod
        elif(np<0):
            ans=(ans*((np//maxi)%mod))%mod
        
        return ans