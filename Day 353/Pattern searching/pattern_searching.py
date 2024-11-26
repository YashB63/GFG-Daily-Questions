def searchPattern(st, pat):
    n=len(st)
    m=len(pat)
    for i in range(n-m+1):
        j=0
        while j<m and pat[j]==st[i+j]:
            j+=1
        if j==m:
            return True
    return False