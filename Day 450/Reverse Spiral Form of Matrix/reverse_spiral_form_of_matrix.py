class Solution:
	def reverseSpiral(self, R, C, mat):
        l,r,t,b=0,len(mat[0]),0,len(mat)
      
        res=[]
        
        while r>l and t<b:
            
            for i in range(l,r):
                res.append(mat[t][i])
            t+=1
            for i in range(t,b):
                res.append(mat[i][r-1])
            r-=1
            if not (l<r and t<b):
                break
            for i in range(r-1,l-1,-1):
                res.append(mat[b-1][i])
            b-=1
            for i in range(b-1,t-1,-1):
                res.append(mat[i][l])
            l+=1
        return res[::-1]