class Solution:

    def Count(self, S):
        
        alpha = ""
        for i in S:
            if i.isalpha():
                alpha += i
        return len(alpha)