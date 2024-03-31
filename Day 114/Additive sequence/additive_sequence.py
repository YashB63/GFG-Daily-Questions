class Solution:
    def isAdditiveSequence(self, n):
        
        def util(a1,a2,s):
            if not s:
                return True
            a=a1+a2
            astr=str(a)
            if not s.startswith(astr):
                return False
            return util(a2,a,s[len(astr):])
        l=len(n)
        for i in range(1,l):
            for j in range(i+1,l):
                a1,a2=int(n[:i]),int(n[i:j])
                if util(a1,a2,n[j:]):
                    return 1
        return 0