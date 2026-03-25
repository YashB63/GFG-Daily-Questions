def greaterElement (arr,  n): 
    temp=sorted(enumerate(arr),key=lambda x:x[1])
    res=[-10000000]*n
    for i in range(n):
        j=i+1
        while j<n:
            if temp[j][1]>temp[i][1]:
                res[temp[i][0]]=temp[j][1]
                break
            j+=1
    return res