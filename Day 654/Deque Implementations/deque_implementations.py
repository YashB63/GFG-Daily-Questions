def pf(dq, x):
    dq.appendleft(x)

def pb(dq, x):
    dq.append(x)

def front_dq(dq):
    if dq:
        return dq[0]
    else:
        return -1

def ppb(dq):
    if dq:
        dq.pop()