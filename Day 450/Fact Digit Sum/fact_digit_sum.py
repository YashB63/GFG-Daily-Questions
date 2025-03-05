from math import factorial as f

class Solution:
	def FactDigit(self, N):
        if N == 1:
            return '1'
        
        lst = []
        
        for i in range(9, 0, -1):
            while N >= f(i):
                lst.append(str(i))  
                N -= f(i)          
        
        lst.sort()
        return ''.join(lst)