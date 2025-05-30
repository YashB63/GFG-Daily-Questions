class Solution():
    def cbaSubsequence(self, s, n):
        lis = [i for i in s]
        lis.sort()
        return "".join(lis)