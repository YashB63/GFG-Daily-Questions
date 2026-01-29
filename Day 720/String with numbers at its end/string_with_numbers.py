class Solution:
    def isSame(self, s):
        letters=0
        numbers=''
        for i in s:
            if i.isalpha():
                letters+=1
            else:
                numbers+=i
        if letters==int(numbers):
            return 1
        else:
            return 0