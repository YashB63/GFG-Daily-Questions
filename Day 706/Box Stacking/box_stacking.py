class Solution:
    def maxHeight(self, height, width, length):
        n = len(height)
        dp = [0 for i in range(10005)]
        rot = []
        for i in range(n):
            a = height[i]
            b = width[i]
            c = length[i]
            rot.append([[a, b], c])
            rot.append([[b, a], c])
            rot.append([[a, c], b])
            rot.append([[c, a], b])
            rot.append([[b, c], a])
            rot.append([[c, b], a])
            rot.sort()
        rot.sort
        for i in range(len(rot)):
            dp[i] = rot[i][1]
            for j in range(i):
                if rot[i][0][0] > rot[j][0][0] and rot[i][0][1] > rot[j][0][1]:
                    dp[i] = max(dp[i], dp[j] + rot[i][1])
        return max(dp)