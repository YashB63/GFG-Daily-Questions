import sys
sys.setrecursionlimit(10**5)

class Solution:
	def findProb(self, N, start_x, start_y, steps):
        def f(x,y,steps):
            if x>=N or x<0 or y>=N or y<0:
                return 0
            if steps==0:
                return 1
            if dp.get((x,y,steps)) is not None:
                return dp[(x,y,steps)]
            count=0
            for i in ((1,2),(-1,2),(1,-2),(-1,-2),(-2,1),(2,1),(2,-1),(-2,-1)):
                count+=f(x+i[0],y+i[1],steps-1)
            dp[(x,y,steps)]= count/8
            return dp[(x,y,steps)]
        dp={}
        return f(start_x,start_y,steps)