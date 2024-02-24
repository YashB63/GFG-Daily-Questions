def findSpecificPattern(dict, pat):
    
    res = []
    x = 1
    xx = 1
    h = 0
    ref = []
    for i in range(len(pat) - 1):
        if pat[i] not in ref:
            ref.append(pat[i])
            xx += 1
        h += (i + 1) * x * xx
        if pat[i + 1] == pat[i]:
            x += 1
        else:
            x = 1
    
    h += len(pat) * x * xx
    for wd in dict:
        x = 1
        tem = 0
        xx = 1
        ref.clear()
        for i in range(len(wd) - 1):
            if wd[i] not in ref:
                ref.append(wd[i])
                xx += 1
            tem += (i + 1) * x * xx
            if wd[i] == wd[i + 1]:
                x += 1
            else:
                x = 1
        tem += len(wd) * x * xx
        if tem == h:
            res.append(wd)
    return res