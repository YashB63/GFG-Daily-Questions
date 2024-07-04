class Solution:
    
    def solve(self, s, ds, res, flag):
        if len(ds)==len(s):
            res.append(ds)
            return
        
        for i in range(len(s)):
            if flag[i]==0 :
                ds+=s[i]
                flag[i]=1
                self.solve(s, ds, res, flag)
                
                ds=ds[:-1]
                flag[i]=0
                
    def find_permutation(self, s):
        
        res=[]
        flag=[0]*len(s)
        self.solve(s, '', res, flag)
        res=list(set(res))
        res.sort()
        return res