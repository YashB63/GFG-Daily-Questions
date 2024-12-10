def Smallestonleft (arr,  n) : 
    def bs(arr,x):
        l,r=0,len(arr)-1
        
        while l<=r:
            m=(l+r)//2
            
            if arr[m]<x:
                l=m+1
            else:
                r=m-1
                
        return l
    
    
    ans=[]
    sl=[-1]*n
    for i in range(n):
        
        pos = bs(ans,arr[i])
        
        if pos>0:
            sl[i]=ans[pos-1]
        
        ans.insert(pos,arr[i])
        
    return sl