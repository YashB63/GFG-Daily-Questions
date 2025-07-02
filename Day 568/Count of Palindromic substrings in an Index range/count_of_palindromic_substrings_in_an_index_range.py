def countPalinInRange (n, A, q1, q2):
    res = 0
    if q1 > q2:
        q1, q2 = q2, q1
    
    for i in range (q1, q2 + 1):
        j = i - 1
        k = i + 1
        
        res += 1
        
        while (j >= q1 and k <= q2):
            if (A[j] == A[k]):
                res += 1
                
            else:
                break
            j -= 1
            k += 1
         
        if (i < n - 1 and A[i] == A[i + 1]):
            j = i
            k = i + 1
            
            while (j >= q1 and k <= q2):
                if (A[j] == A[k]):
                    res += 1
                else:
                    break
                j -= 1
                k += 1             
    return res