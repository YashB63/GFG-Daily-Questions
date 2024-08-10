class Solution:
    def reverseWords(self, S):
        S=S.split(".")
        S=S[::-1]
        S=".".join(S)
        return S