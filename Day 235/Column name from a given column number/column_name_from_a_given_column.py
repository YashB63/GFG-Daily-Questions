class Solution:
    def colName (self, n):
        result = []
        while n > 0:
            n -= 1
            result.append(chr(n % 26 + ord('A')))
            n //= 26
        return ''.join(result[::-1])
