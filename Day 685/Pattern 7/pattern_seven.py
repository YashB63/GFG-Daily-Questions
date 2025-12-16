class Solution:
    def printTriangle(self, N):
        for row in range(1, 1 + N):
            for space in range(N - row):
                print(' ', end = '')
            for asterisk in range(1, 2 * row):
                print('*', end = '')
            print()