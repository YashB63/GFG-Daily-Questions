class Solution:
    def secondSmallest(self, S, D):
        if D==1 and S<=9:
            return S
            
        if S > 9 * D or S < 1:
            return -1

        digits = [0] * D
        S -= 1  
        for i in range(D - 1, 0, -1):
            if S > 9:
                digits[i] = 9
                S -= 9
            else:
                digits[i] = S
                S = 0
        digits[0] = S + 1  

        for i in range(D - 1, 0, -1):
            if digits[i] > 0 and digits[i - 1] < 9:
                digits[i] -= 1
                digits[i - 1] += 1
                break
        else:
            return -1  

        return ("".join(map(str, digits)))