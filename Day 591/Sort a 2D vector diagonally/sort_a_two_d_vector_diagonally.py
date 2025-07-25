class Solution:
    def diagonalSort(self, matrix, n, m):
        lower_triangle = [[] for i in range(n)]
        upper_triangle = [[] for i in range(m)]

        major_diagonal = []

        for i in range(n):
            for j in range(m):
                if j < i :
                    lower_triangle[i-j].append(matrix[i][j])
                elif j>i :
                    upper_triangle[j-i].append(matrix[i][j])
                else :
                    major_diagonal.append(matrix[i][j])

        for i in range(n):
            lower_triangle[i].sort()
            lower_triangle[i] = lower_triangle[i][::-1]

        for i in range(m):
            upper_triangle[i].sort()

        for i in range(n):
            for j in range(m):
                if j<i :
                    d = i-j
                    l = len(lower_triangle[d])-1
                    matrix[i][j] = lower_triangle[d][l]
                    lower_triangle[d].pop()
                elif j>i : 
                    d = j-i
                    l = len(upper_triangle[d])-1
                    matrix[i][j] = upper_triangle[d][l]
                    upper_triangle[d].pop()