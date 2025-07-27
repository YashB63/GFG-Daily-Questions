class Solution:
    def findStrictlyIncreasingNum(self, start, out, n, ans):
        if n == 0:
            ans.append(int(out))
            return

        for i in range(start, 10):
            self.findStrictlyIncreasingNum(i + 1, out + str(i), n - 1, ans)

    def increasingNumbers(self, N):
        ans = []
        self.findStrictlyIncreasingNum(0, "", N, ans)

        ret = []
        for num in ans:
            if len(str(num)) == N:
                ret.append(num)
        return ret