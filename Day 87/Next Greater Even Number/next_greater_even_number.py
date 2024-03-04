class Solution:
    def getNextEven(self,x):
    	  
	    s,p,flag,r = [],0,0,int(x)
        for i in x:
            p +=int(i)
            if int(i)%2==0:
                flag=1
            s.append(i)
        
        if flag==0:
            return -1
         
        n,x = len(s),int(x)
        
        while r%2!=0 or r<=x:
            l,k = -1,-1
            for i in range(n-2,-1,-1):
                if s[i]<s[i+1]:
                    k = i
                    break
            if k==-1:
                return -1
            
            for i in range(k+1,n):
                if s[k]<s[i]:
                    l = i
                   
            
            s[k],s[l] = s[l],s[k]
            s = s[:k+1]+s[k+1:][::-1]
            r = int(''.join(s))
            
        return r