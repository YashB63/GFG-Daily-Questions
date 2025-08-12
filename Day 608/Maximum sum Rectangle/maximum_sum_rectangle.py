class Solution:
    def kadane(self, temp):
        rows = len(temp)

        currSum = 0
        maxSum = float('-inf')

        for i in range(rows):
            currSum += temp[i]

            if maxSum < currSum:
                maxSum = currSum

            if currSum < 0:
                currSum = 0

        return maxSum

    def maxRectSum(self, mat):
        rows = len(mat)
        cols = len(mat[0])

        maxSum = float('-inf')

        temp = [0] * rows

        for left in range(cols):
            temp = [0] * rows

            for right in range(left, cols):
                for row in range(rows):
                    temp[row] += mat[row][right]

                sumValue = self.kadane(temp)

                maxSum = max(maxSum, sumValue)

        return maxSum