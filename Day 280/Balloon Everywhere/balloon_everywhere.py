class Solution:
    def maxInstance(self, s : str) -> int:
        b=s.count('b')

        a=s.count('a')

        l=s.count('l')//2

        o=s.count('o')//2

        n=s.count('n')

        return min(b,a,l,o,n)