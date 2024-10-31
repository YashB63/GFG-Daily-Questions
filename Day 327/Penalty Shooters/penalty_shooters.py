class Solution:
    def goals(self, X, Y, Z):
        p =0
        q =0
        while Z>1:
            if (X%Z != 0 and Y%Z != 0):
                Z=Z-1
            elif(X%Z == 0 and Y%Z != 0):
                X-=1
                p+=1
            elif(Y%Z == 0 and X%Z != 0):
                Y-=1
                q+=1
            elif(X%Z == 0 and Y%Z == 0):
                X-=1
                p+=1
        return p,q
