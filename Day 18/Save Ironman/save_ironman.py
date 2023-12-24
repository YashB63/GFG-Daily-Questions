def saveIronman (s) : 
    
    a = []
    for i in s:
        if i.isalpha() or i.isnumeric():
            a.append(i.upper())
    b = a[::-1]
    return a == b