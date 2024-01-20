def uneatenLeaves(arr,n,k):
      
    res = [1 for i in range(n + 1)]
    res[0] = 0
    for i in range(len(arr)):
        if(arr[i] <= n and res[arr[i]]==1):
            for j in range(arr[i], n+1, arr[i]):
                res[j]=0
    return sum(res)