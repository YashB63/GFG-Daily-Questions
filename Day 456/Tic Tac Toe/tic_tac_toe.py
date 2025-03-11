class Solution:
    def __init__(self):
        self.win = [
            [0, 1, 2],  
            [3, 4, 5],  
            [6, 7, 8],  
            [0, 3, 6],  
            [1, 4, 7],  
            [2, 5, 8],  
            [0, 4, 8],  
            [2, 4, 6]  
        ]

    
    def is_c_win(self, board, c):
        count = 0
        for i in range(8):
            if board[self.win[i][0]] == c and board[
                    self.win[i][1]] == c and board[self.win[i][2]] == c:
                count += 1
        return count

    
    def isValid(self, board):
        
        x_count = board.count('X')
        o_count = board.count('O')

        cx = self.is_c_win(board, 'X')
        co = self.is_c_win(board, 'O')

        if x_count != o_count + 1:
            return False

        if co == 1 and cx == 0:
            return True

        if cx == 1 and co == 0:
            return True

        if cx == 0 and co == 0:
            return True

        return False