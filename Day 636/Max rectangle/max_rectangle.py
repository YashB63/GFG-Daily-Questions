class Solution:
    def maxHist(self, row, C):
        result = list()
        top_val = 0  
        max_area = 0  
        area = 0  

        i = 0
        while (i < C):
            if (len(result) == 0) or (row[result[-1]] <= row[i]):
                result.append(i)
                i += 1
            else:
                top_val = row[result[-1]]
                result.pop()
                area = top_val * i

                if (len(result)):
                    area = top_val * (i - result[-1] - 1)
                max_area = max(area, max_area)

        while (len(result)):
            top_val = row[result[-1]]
            result.pop()
            area = top_val * i
            if (len(result)):
                area = top_val * (i - result[-1] - 1)

            max_area = max(area, max_area)

        return max_area

    def maxArea(self, mat):
        R = len(mat)
        C = len(mat[0])
        result = self.maxHist(mat[0], C)

        for i in range(1, R):
            for j in range(C):
                if (mat[i][j]):
                    mat[i][j] += mat[i - 1][j]
            result = max(result, self.maxHist(mat[i], C))

        return result