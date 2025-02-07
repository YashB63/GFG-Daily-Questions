class Solution:
    
    def solveSudoku(self, mat):
        rw=[0]*9
        for y in range(9):
            for ve in mat[y]:
                if ve>0:
                    rw[y]+=1<<ve
        cl=[0]*9
        for x in range(9):
            for ve in list(zip(*mat))[x]:
                if ve>0:
                    cl[x]+=1<<ve
        sq=[[0]*3 for _ in range(3)]
        for y in range(9):
            for x in range(9):
                ve=mat[y][x]
                if ve>0:
                    sq[y//3][x//3]+=1<<ve
                    
        def bt(x=0,y=0):
            nonlocal mat,rw,cl,sq
            if y==9:
                return True
            nx=x+1
            ny=y
            if nx>=9:
                nx=0
                ny=y+1
            if mat[y][x]==0:
                for cand in range(1,10):
                    if (1<<cand)&rw[y]:
                        continue
                    if (1<<cand)&cl[x]:
                        continue
                    if (1<<cand)&sq[y//3][x//3]:
                        continue
                    rw[y]+=1<<cand
                    cl[x]+=1<<cand
                    sq[y//3][x//3]+=1<<cand
                    mat[y][x]=cand
                    if bt(nx,ny):
                        return True
                    rw[y]-=1<<cand
                    cl[x]-=1<<cand
                    sq[y//3][x//3]-=1<<cand
                    mat[y][x]=0
                return False
            return bt(nx,ny)
        bt()
        return mat