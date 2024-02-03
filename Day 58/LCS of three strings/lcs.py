from functools import lru_cache

class Solution:

    def LCSof3(self,A,B,C,n1,n2,n3):
        
        @lru_cache(None)
        def common(s1, s2, s3, i, j, k):
            if i == n1 or j == n2 or k == n3:
                return 0
            if s1[i] == s2[j] == s3[k]:
                return 1 + common(s1, s2, s3, i+1, j+1, k+1)
            k1 = common(s1, s2, s3, i+1, j, k)
            k2 = common(s1, s2, s3, i, j+1, k)
            k3 = common(s1, s2, s3, i, j, k+1)
            return max(k1, k2, k3)
            
        return common(A, B, C, 0, 0, 0)