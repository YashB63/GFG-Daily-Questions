class Solution:
    def roundToNearest (self, s) : 
        s = list(s)
        l = int(s[-1])
        if l <= 5:
            s[-1] = '0'
            return ''.join(s)
        else:
            carry = 1
            s.reverse()
            s[0] = '0'
            for i in range(1,len(s)):
                d = int(s[i])
                r = d+carry
                s[i] = str(r%10)
                carry = r//10
                if carry == 0: break
            if carry: s.append(str(carry))
            s.reverse()
            return ''.join(s)