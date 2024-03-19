class Solution:
    def largestSubsquare(self, n, a):
        
        top = [[0 for _ in range(n)] for _ in range(n)]
        left = [[0 for _ in range(n)] for _ in range(n)]
        maxSubSq=0
        for i in range(n):
            for j in range(n):
                if a[i][j] == 'X':
                    if i > 0:
                        top[i][j] = top[i - 1][j] + 1
                    else:
                        top[i][j] = 1
                    if j > 0:
                        left[i][j] = left[i][j - 1] + 1
                    else:
                        left[i][j] = 1
                    for k in range(min(top[i][j], left[i][j]), maxSubSq, -1):
                        if top[i][j - k + 1] >= k and left[i - k + 1][j] >= k:
                            maxSubSq = max(maxSubSq, k)
                            break

        return maxSubSq