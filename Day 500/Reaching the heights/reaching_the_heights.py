def reaching_height (n, arr) : 
    if n==1:
        return arr
    if len(set(arr))==1:
        return [-1]
    arr.sort()
    start=0
    end=len(arr)-1
    new=[]
    while start<=end:
        if start==end:
            new.append(arr[start])
        else:
            new.append(arr[end])
            new.append(arr[start])
        start+=1
        end-=1
    return new