class Solution:
    def convertRoman(self, n):
        
        x = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        s = ''
        for i in range(len(x)):
            while n >= x[i][0]:
                s += x[i][1]
                n -= x[i][0]
        
        return s