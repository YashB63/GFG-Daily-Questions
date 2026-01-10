class Solution:
    def help(self,mat,x):
        n=len(mat)
        i,j=0,n-1
        ans=0
        while j>=0 and i<=n-1:
            if mat[i][j]>x:
                j-=1
            else:
                i+=1
                ans+=(j+1)
        return ans

    def kthSmallest(self, mat, k):
        n=len(mat)
        l,h=mat[0][0],mat[n-1][n-1]
        while l<=h:
            mid=(l+h)//2
            if self.help(mat,mid)>=k:
                h=mid-1
            else:
                l=mid+1
        return h+1