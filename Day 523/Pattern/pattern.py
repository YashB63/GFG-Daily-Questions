class Solution:
    def printDiamond(self, N):
        for row in range(1, N + 1):
            for space in range(N - row):
                print(' ', end = '')
            
            for asterisk in range(1, row + 1):
                print('* ', end = '')
            print()
        
        for row in range(N, 0, -1):
            for space in range(N - row):
                print(' ', end = '')
                
            for asterisk in range(1, row + 1):
                print('* ', end = '')
            print()