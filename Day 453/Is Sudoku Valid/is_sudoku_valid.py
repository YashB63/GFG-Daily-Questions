class Solution:
    def isValid(self, mat):
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        subgrid_sets = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                num = mat[i][j]
                if num == 0:
                    continue  

                if (num in row_sets[i] or
                    num in col_sets[j] or
                    num in subgrid_sets[i//3][j%3]):
                    return False
                
                row_sets[i].add(num)
                col_sets[j].add(num)
                subgrid_sets[i//3][j//3].add(num)

        return True