class Solution:
	def solveQueries(self, n, Queries):
	    matrix=[[0]*(n+2) for _ in range(n+2)]
	    row=[[0]*(n+2) for _ in range(n+2)]
	    col=[[0]*(n+2) for _ in range(n+2)]
	    
	    for i in Queries:
	        a=i[0]
	        b=i[1]
	        c=i[2]
	        d=i[3]
	        
	        row[a][b]+=1
	        row[c+1][b]-=1
	        col[a][d+1]-=1
	        col[c+1][d+1]+=1
	        
	    for i in range(n):
	        for j in range(1,n):
	            row[j][i]+=row[j-1][i]
	            col[j][i]+=col[j-1][i]
	            
	    for i in range(n):
	        matrix[i][0]=row[i][0]+col[i][0]
	    for i in range(1,n):
	        for j in range(n):
	            matrix[j][i]+=matrix[j][i-1]+row[j][i]+col[j][i]
	            
	    res=[[0]*(n) for _ in range(n)]
	    for i in range(n):
	        for j in range(n):
	            res[i][j]=matrix[i][j]
	            
	    return res