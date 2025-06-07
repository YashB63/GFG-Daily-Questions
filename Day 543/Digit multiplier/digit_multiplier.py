class Solution:
    def getSmallest(self, N):
        if N == 0:
            return "10"  
        if N == 1:
            return "1"

        digits = []
        for d in range(9, 1, -1):
            while N % d == 0:
                digits.append(d)
                N //= d

        if N != 1:
            return "-1"

        digits.sort()
        return ''.join(map(str, digits))