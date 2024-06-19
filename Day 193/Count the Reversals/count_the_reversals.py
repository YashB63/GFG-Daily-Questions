from collections import deque

def countRev (s):
   
    if(len(s)%2!=0):
        return -1
    q=deque()
    for i in s:
        if(i=="{"):
            q.append("{")
        else:
            if(len(q)>0 and q[-1]=="{"):
                q.pop()
                continue
            else:
                q.append("}")
    
    res=0
    while q:
        b1=q.popleft()
        b2=q.popleft()
        if(b1=="}"):
            res+=1
            if(b2=="{"):
                res+=1
        elif(b1=="{"):
            if(b2=="{"):
                res+=1
    return res
