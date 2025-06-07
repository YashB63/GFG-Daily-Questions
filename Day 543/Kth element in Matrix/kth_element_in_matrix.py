class Solution:
    def count_smaller_equal(self, matrix, x):
        n = len(matrix)
        count = 0
        row, col = 0, n - 1

        while row < n and col >= 0:
            if matrix[row][col] <= x:
                count += (col + 1)
                row += 1
            else:
                col -= 1

        return count

    def kthSmallest(self, matrix, k):
        n = len(matrix)
        low, high = matrix[0][0], matrix[n - 1][n - 1]
        ans = 0

        while low <= high:
            mid = low + (high - low) // 2

            count = self.count_smaller_equal(matrix, mid)

            if count < k:
                low = mid + 1
            else:
                ans = mid
                high = mid - 1

        return ans