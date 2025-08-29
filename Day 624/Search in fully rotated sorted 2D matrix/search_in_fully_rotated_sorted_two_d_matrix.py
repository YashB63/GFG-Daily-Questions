class Solution:
    def searchMatrix(self, mat, x):
        n = len(mat)
        m = len(mat[0])

        low, high = 0, n * m - 1

        while low <= high:
            mid = low + (high - low) // 2

            row = mid // m
            col = mid % m
            midVal = mat[row][col]

            if midVal == x:
                return True

            lowRow = low // m
            lowCol = low % m
            lowVal = mat[lowRow][lowCol]

            if lowVal <= midVal:
                if lowVal <= x < midVal:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                highRow = high // m
                highCol = high % m
                highVal = mat[highRow][highCol]

                if midVal < x <= highVal:
                    low = mid + 1
                else:
                    high = mid - 1

        return False
