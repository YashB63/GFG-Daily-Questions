class Solution:
    def rotate(self, N, D):
        
        x = len(bin(N)[2:])
        bin_n = '0'*(16-x) + bin(N)[2:]
        
        res = [0]*2
        D = D%16
        res[0] = int(bin_n[D:] + bin_n[:D], 2)
        res[1] = int(bin_n[-D:] + bin_n[:-D], 2)
        
        return res