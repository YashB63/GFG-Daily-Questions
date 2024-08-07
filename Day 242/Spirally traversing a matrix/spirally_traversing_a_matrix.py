class Solution:
    def spirallyTraverse(self, matrix):
        a, r, t, b = 0, len(matrix[0])-1, 0, len(matrix)-1
        result = []
        while a <= r and t <= b:
            for i in range(a, r+1):
                result.append(matrix[t][i])
            t += 1
            for i in range(t, b+1):
                result.append(matrix[i][r])
            r -= 1
            if t <= b:
                for i in range(r, a-1, -1):
                    result.append(matrix[b][i])
                b -= 1
            if a <= r:
                for i in range(b, t-1, -1):
                    result.append(matrix[i][a])
                a += 1
        return result
