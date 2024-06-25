class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr,n):
        
        l=[x for x in arr if x>0]
        l.sort()
        
        if len(l)==0 or l[0]!=1:
            return 1
            
        else:
            
            for i in range(1,len(l)):
                if l[i]-l[i-1]==0 or l[i]-l[i-1]==1:
                    continue
                else:
                    return l[i-1]+1
                
        return l[-1]+1