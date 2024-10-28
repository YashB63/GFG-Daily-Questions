from itertools import permutations

class Solution:
    def maxPerm(self, N , M):
        maxi = -1
        
        for k in list(permutations(str(N))):
            k= int("".join(k))
            if k>maxi and k<=M:
                maxi = max(maxi, k)
                

        return maxi