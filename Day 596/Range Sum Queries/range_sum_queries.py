def updateValueUtil(st, ss, se, i, val, si) :
    if ss==i and se==i:
        st[si]=val
        return
    
    if ss>i or se< i:
        return
    
    mid=ss + (se -ss) // 2
    
    updateValueUtil(st,ss,mid,i,val,si*2+1)
    updateValueUtil(st,mid+1,se,i,val,si*2+2)
    
    st[si]=st[2*si+1]+st[2*si+2]
    
def updateValue(arr, st, n, i, new_val) :  
    if (i < 0 or i > n - 1) : 
        return
  
    updateValueUtil(st, 0, n - 1, i,new_val, 0)   

def getSumUtil(st, ss, se, qs, qe, si) :  
    if ss>=qs and se<=qe:
        return st[si]
    
    if qe<ss or se<qs:
        return 0
    
    mid=ss+(se-ss)//2
    
    return getSumUtil(st,ss,mid,qs,qe,si*2+1)+getSumUtil(st,mid+1,se,qs,qe,si*2+2)
    
    

def getSum(st, n, qs, qe) :  
    if (qs < 0 or qe > n - 1 or qs > qe) :
        return -1;  
      
    return getSumUtil(st, 0, n - 1, qs, qe, 0)
