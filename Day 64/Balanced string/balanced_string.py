class Solution:
    def BalancedString(self,N):
        #code here
        
        count = 0
        x = str(N)
        
        for c in x:
            count += int(c)
        
        alpha = [chr(i) for i in range(97, 123)]
        rev = alpha[::-1]
        q, N = divmod(N, 26)
        res = q * ''.join(alpha)
        if N == 0:
            return res
        if N & 1:
            if count % 2 != 0:
                first = (N - 1) // 2
                second = (N + 1) // 2
            
            else:
                second = (N - 1) // 2
                first = (N + 1) // 2
        
        else:
            first = second = N // 2
        
        res += ''.join(alpha[:first]) + ''.join(rev[:second][::-1])
        return res