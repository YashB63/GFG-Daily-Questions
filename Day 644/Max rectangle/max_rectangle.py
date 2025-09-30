class Solution:
    def getMaxArea(self, arr):
        n = len(arr)
        s = []
        res = 0

        for i in range(n):
            while s and arr[s[-1]] >= arr[i]:

                tp = s.pop()
                width = i if not s else i - s[-1] - 1

                res = max(res, arr[tp] * width)
            s.append(i)

        while s:
            tp = s.pop()
            curr = arr[tp] * (n if not s else n - s[-1] - 1)
            res = max(res, curr)

        return res

    def maxArea(self, mat):
        n = len(mat)
        m = len(mat[0])

        arr = [0] * m
        ans = 0

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    arr[j] += 1
                else:
                    arr[j] = 0

            ans = max(ans, self.getMaxArea(arr))

        return ans