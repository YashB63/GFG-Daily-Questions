def printFirstNegativeInteger( A, N, K):
    i=0
    j=0
    sw=[]
    ar=[]
    while(j<N):
        if(j-i<K):
            if(A[j]<0):
                sw.append(A[j])
            j+=1
        
        if(j-i==K):
            if len(sw)==0:
                ar.append(0)
            else:
                ar.append(sw[0])
                
                if A[i] == sw[0]:
                    sw.pop(0)
            i+=1
    return ar