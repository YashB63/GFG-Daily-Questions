class Solution:
	def MinimumExchange(self, matrix):
        t1=0
        t2=0
        for x in range(n):
            for y in range(m):
                if ((x+y)%2==0 and matrix[x][y]=="A") or ((x+y)%2==1 and matrix[x][y]=="B"):
                    t2+=1
                else:
                    t1+=1
        if t1%2==1:
            return t2//2
        elif t2%2==1:
            return t1//2
        return(min(t1,t2)//2)