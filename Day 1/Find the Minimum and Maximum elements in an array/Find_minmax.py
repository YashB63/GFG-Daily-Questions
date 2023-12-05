def getMinMax(a, n):
    if n == 0:
        return -1 -1
        
    minimum = a[0]
    maximum = a[0]
    
    for i in range(1,n):
        if a[i] < minimum:
            minimum = a[i]
        elif a[i] > maximum:
            maximum = a[i]
            
    return minimum, maximum