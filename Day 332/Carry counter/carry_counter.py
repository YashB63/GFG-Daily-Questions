class Solution:
    def getCarries(self, N, M):
        p = str(N)
        q = str(M)
        a = len(p)
        b = len(q)
        c = 0
        carry_count = 0
        for i in range(1, max(a, b) + 1):
            if i<=a:
                digit_n = int(p[-i])
            else:
                digit_n=0
            if i<=b:
                digit_m = int(q[-i])
            else:
                digit_m=0
            total = digit_n + digit_m + c
            if total >= 10:
                carry_count += 1
                c = total // 10 
            else:
                c = 0 
        
        return carry_count