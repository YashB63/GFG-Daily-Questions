class Solution:

	def nthRowOfPascalTriangle(self, n):
        lst=[1]
        
        def check(lt):
            n=len(lt)
            res=[1]*(n+1)
            for i in range(1,n):
                res[i]=lt[i]+lt[i-1]
            return res
            
        for i in range(1,n):
            lst=check(lst)
        return lst