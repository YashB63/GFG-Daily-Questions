class Solution:
    def constructLinkedMatrix(self, mat):
        n = len(mat)
        m = len(mat[0])
        linked_list_mat = [[None] * m for _ in range(n)]
        for r in range(n):
            for c in range(m):
                linked_list_mat[r][c] = Node(mat[r][c])
                if c - 1 >= 0:
                    linked_list_mat[r][c - 1].right = linked_list_mat[r][c]
                    
                if r - 1 >= 0:
                    linked_list_mat[r - 1][c].down = linked_list_mat[r][c]
        
        return linked_list_mat[0][0]