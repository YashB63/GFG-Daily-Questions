class Solution:
    def find(self,A,B): 
        while A>0:
            A=A+1
            if(B>0 and A%B==0):
                break
            
        return A