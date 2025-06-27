class Solution:
    def rotateMatrix(self, M, N, Mat):
        row,col=0,0
        a,b=M,N
        prev,curr=0,0
        
        while row<M and col<N:
            if row+1==M or col+1==N:
                break
            
            prev = Mat[row+1][col];
            
            for i in range(col,N):
                curr=Mat[row][i]
                Mat[row][i]=prev
                prev=curr
                
            row+=1
            
            for i in range(row,M):
                curr=Mat[i][N-1]
                Mat[i][N-1]=prev
                prev=curr
                
            N-=1
            
            if row<M:
                for i in range(N-1,col-1,-1):
                    curr=Mat[M-1][i]
                    Mat[M-1][i]=prev
                    prev=curr
            
            M-=1
            
            if col<N:
                for i in range(M-1,row-1,-1):
                    curr=Mat[i][col]
                    Mat[i][col]=prev
                    prev=curr
                    
            col+=1
             
        return Mat