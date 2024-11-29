class Solution:
    def assignMiceHoles(self, N , M , H):
        mice = sorted(M)
        holes = sorted(H)
        temp = 0
        ans = float('-inf')
        while temp < N:
            ans = max(ans, abs(holes[temp] - mice[temp]))
            temp += 1
        return ans