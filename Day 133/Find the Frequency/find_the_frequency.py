def findFrequency (arr, n, x):
    
    c=0
    for i in arr:
        if i==x:
            c+=1
    return c