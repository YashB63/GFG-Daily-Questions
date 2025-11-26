class Solution:
    def convert(self, s):
        chars = list(s)

        for i in range(len(chars)):
            if i == 0 or chars[i - 1] == ' ':
                chars[i] = chars[i].upper()  

        return ''.join(chars)