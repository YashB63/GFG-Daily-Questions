class Solution:
    def yShapedPattern(self, N):
        s= ""
        for i in range(1,int(N/2)+1):
            s+=" "*(i-1)
            s+="*"+" "*(N+1-2*i)+"*"
            s+="\n"
        for i in range(int(N/2)+1,N+1):
            s+=" "*(N-2) +"*"+" "*(N-2)
            if i!=N:
                s+="\n"
        return s