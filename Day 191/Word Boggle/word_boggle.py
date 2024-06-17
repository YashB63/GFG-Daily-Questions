class Solution:
    def wordBoggle(self,board,dictionary):
       
        Rows = len(board)
        Cols = len(board[0])
        
        
        def dfs(r,c,i,word):
            
            if i == len(word):
                return True
                
               
            if r < 0 or r == Rows or c < 0 or c == Cols or (r,c) in seen or board[r][c] != word[i]:
                return False
                
            
            seen.add((r,c))
            
            down = dfs(r+1,c,i+1,word)
            up = dfs(r-1,c,i+1,word)
            right = dfs(r,c+1,i+1,word)
            left = dfs(r,c-1,i+1,word)
            
            
            downright = dfs(r+1,c+1,i+1,word)
            downleft = dfs(r-1,c-1,i+1,word)
            upright = dfs(r-1,c+1,i+1,word)
            upleft = dfs(r+1,c-1,i+1,word)
            
            
            
            seen.remove((r,c))
            
            return down or up or right or left or downright or downleft or upright or upleft
        
        
        res = []
        seen = set()
        for w in dictionary:
            for r in range(Rows):
                for c in range(Cols):
                    if board[r][c] == w[0]:
                        
                        if dfs(r,c,0,w):
                            res.append(w)
                            break
        return list(set(res))
