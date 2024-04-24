def find4Numbers( A, n, X):
    
    A.sort()
    
    for  j in range(0,n-3):
        
        X1 = X - A[j]
        
        
        
        for i in range(j+1,n-2):
            
            ans = X1 - A[i]
            start = i + 1
            end   = n-1
            
            while(start < end):
                
                if( A[start]  + A[end] == ans):
                    return 1;
                    
                elif(A[start] + A[end] > ans):
                    end -= 1
                    
                else:
                    start += 1
                    
                    
    return 0