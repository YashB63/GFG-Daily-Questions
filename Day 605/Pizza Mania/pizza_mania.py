from functools import lru_cache

class Solution:
    def getPizza(self, X, S, M, L, CS, CM, CL):
        @lru_cache(maxsize=None)
        def dp(currcost, X):
            if X <= 0:
                return currcost

            ans1 = dp(currcost + CS, X - S)
            ans2 = dp(currcost + CM, X - M)
            ans3 = dp(currcost + CL, X - L)

            return min(ans1, ans2, ans3)

        return dp(0, X)