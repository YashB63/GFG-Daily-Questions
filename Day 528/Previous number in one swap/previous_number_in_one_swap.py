class Solution:
    def previousNumber(ob,S):
        index = -1
        S=list(S)
        n=len(S)
        
        for i in range(n - 2, -1, -1): 
            if int(S[i]) > int(S[i + 1]): 
                index = i 
                break
      
        smallGreatDgt = -1
        for i in range(n - 1, index, -1): 
            if (smallGreatDgt == -1 and int(S[i]) <  
                                        int(S[index])): 
                smallGreatDgt = i 
            elif (index > -1 and int(S[i]) >= 
                                 int(S[smallGreatDgt]) and 
                                 int(S[i]) < int(S[index])): 
                smallGreatDgt = i 
          
        if index == -1: 
            return "" . join("-1") 
        else:  
            (S[index],  S[smallGreatDgt]) = (S[smallGreatDgt],  S[index]) 
        if S[0]=='0':
            return '-1'
        return "" . join(S)