class Solution:
    def findIndex(self,str):
        n=len(str)
        
        open_count=[0]*(n+1)
        close_count=[0]*(n+1)
        
        for i in range(1,n+1):
            open_count[i]=open_count[i-1]+(1 if str[i-1]=='(' else 0)
            
        for i in range(n-1,-1,-1):
            close_count[i]=close_count[i+1]+(1 if str[i]==')' else 0)
            
        for i in range(n+1):
            if open_count[i]==close_count[i]:
                return i
                
        return -1