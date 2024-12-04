class Solution:
    def myAtoi(self, s):
        s = s.strip()  
        if not s:
            return 0

        sign = 1
        if s[0] == '-':  
            sign = -1
            s = s[1:]
        elif s[0] == '+':  
            s = s[1:]

        result = 0
        for char in s:
            if char.isdigit():
                result = result * 10 + int(char)
                if sign == 1 and result > 2**31 - 1:
                    return 2**31 - 1
                if sign == -1 and result > 2**31:
                    return -2**31
            else:
                break

        return sign * result