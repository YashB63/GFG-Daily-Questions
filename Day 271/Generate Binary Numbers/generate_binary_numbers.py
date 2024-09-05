def generate(N):
    l=[]
    for i in range(1,N+1):
        res=bin(i)
        l.append(res[2:])
    return l