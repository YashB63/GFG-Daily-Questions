from functools import lru_cache

class Solution:
	def minOperations(self, str1, str2):
        m,n = len(str1),len(str2)
        @lru_cache(None)
        def dfs(i,j):
            if i == m or j==n:
                return abs(m-i + n-j)
            if str1[i] == str2[j]:
                return dfs(i+1,j+1)
            return 1 + min(dfs(i,j+1),dfs(i+1,j))
        return dfs(0,0)