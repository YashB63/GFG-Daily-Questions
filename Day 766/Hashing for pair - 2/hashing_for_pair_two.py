def sumExists(arr, N, sum):
    s=list(set(arr))
    n=len(s)
    for i in range(n):
        if sum-s[i] in s[i+1:n]:
            return 1
    return 0