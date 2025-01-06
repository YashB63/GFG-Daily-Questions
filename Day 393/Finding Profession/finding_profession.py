class Solution:
    def profession(self, level, pos):
        if pos == 1: return 'e'
        if pos == 2: return 'd'
        x=self.profession(level-1,(pos+1)//2)
        if pos%2 == 0:
            return chr(ord(x)^ord('e')^ord('d'))
        else:
            return x