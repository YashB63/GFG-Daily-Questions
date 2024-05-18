class Solution:
    def toh(self, N, fromm, to, aux):
        
        if N == 0:
            return 0
        moves1 = self.toh(N-1,fromm,aux,to)
        print("move disk",N,"from rod",fromm,"to rod",to)
        moves2 = self.toh(N-1,aux,to,fromm)
        return moves1 + moves2 + 1