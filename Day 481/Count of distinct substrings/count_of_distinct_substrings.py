def countDistinctSubstring(s):
    res=set()
    for i in range(len(s)):
        ss=""
        
        for j in range(i, len(s)):
            ss=ss+s[j]
            res.add(ss)
    return len(res)+1