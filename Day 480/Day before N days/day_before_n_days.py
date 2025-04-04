import math

def nthDay(d, n):
    k=n%7
    r=d-k
    if(r<0):
        r+=7
    return r