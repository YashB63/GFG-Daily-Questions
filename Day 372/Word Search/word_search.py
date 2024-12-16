class Solution:
	def isWordExist(self, board, word):
        n=len(board)
        m=len(board[0])
        o=len(word)
        visited=[[False for i in range(m)] for i in range(n)]
        delrow=[-1,1,0,0]
        delcol=[0,0,-1,1]
        def answer(i,j,k):
            if k==o:
                return True
            visited[i][j]=True
            for d in range(4):
                r=delrow[d]+i
                c=delcol[d]+j
                if 0<=r<n and 0<=c<m and not visited[r][c] and board[r][c]==word[k] :
                    if answer(r,c,k+1):
                        return True
            visited[i][j]=False
            return False
        for i in range(n):
            for j in range(m):
                if board[i][j]==word[0] and answer(i,j,1):
                    return True
        return False