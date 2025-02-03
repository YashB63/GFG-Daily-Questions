class Solution:
    def findK(self, a, n, m, k):
        ans=[]
        left=0
        right=m-1
        top=0
        bottom=n-1
        while(left<=right and top<=bottom):
            for i in range(left,right+1):
                ans.append(a[top][i])
            top+=1
            for i in range(top,bottom+1):
                ans.append(a[i][right])
            right-=1
            if (top<=bottom):
                for i in range(right,left-1,-1):
                    ans.append(a[bottom][i])
                bottom-=1
            if (left<=right):
                for i in range(bottom,top-1,-1):
                    ans.append(a[i][left])
                left+=1
        return ans[k-1]