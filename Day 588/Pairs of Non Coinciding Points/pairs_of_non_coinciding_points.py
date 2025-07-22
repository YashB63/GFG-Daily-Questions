from collections import Counter

class Solution:
    def numOfPairs(self, X, Y, N):
        xseen = Counter()
        yseen = Counter()
        seen = set()
        same = 0

        for i in range(N):
            xseen[X[i]] += 1
            yseen[Y[i]] += 1
            
            if (X[i], Y[i]) in seen:
                same += 2
            else:
                seen.add((X[i], Y[i]))
            
        ans = 0

        for k, v in xseen.items():
            ans += (v*(v-1))//2
            
        for k, v in yseen.items():
            ans += (v*(v-1))//2
            
        return ans - same 