class Solution:
    def findK(self, mat, n, m, k):
        top,bot=0,n-1
        left,right=0,m-1
        l=[]
        while top<=bot and left<=right:
            for i in range(left,right+1):
                l.append(mat[top][i])
            top+=1
            for i in range(top,bot+1):
                l.append(mat[i][right])
            right -=1
            if top<=bot:
                for i in range(right,left-1,-1):
                    l.append(mat[bot][i])
                bot-=1
            if left<=right:
                for i in range(bot,top-1,-1):
                    l.append(mat[i][left])
                left+=1
        return l[k-1]