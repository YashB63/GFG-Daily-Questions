def LargButMinFreq(arr,n):
    
    d=dict()
    a=[]
    b=[]
    for i in range(n):
        if arr[i] in d:
            d[arr[i]]+=1
        else:
            d[arr[i]]=1
    for i in d:
        a.append(d[i])
    s=min(a)
    for i in d:
        if d[i]==s:
           b.append(i)
        
    return max(b)