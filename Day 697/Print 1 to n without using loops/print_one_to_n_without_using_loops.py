class Solution:
    def printTillN(self, N):
        if(N == 0):
            return
        else:
            self.printTillN(N-1)
            print(N, end=" ")