class Solution:
    def maximumSumRectangle(self,mat):
        max_sum = -float('inf')
        R, C = len(mat), len(mat[0])
        M = mat

        for i in range(C):
            cumulative_col = [0] * R
            for j in range(i, C):
                cur_sum = 0
                for row in range(R):
                    cumulative_col[row] += M[row][j]
                    cur_sum = max(cumulative_col[row], cumulative_col[row] + cur_sum)
                    max_sum = max(max_sum, cur_sum)
        return max_sum