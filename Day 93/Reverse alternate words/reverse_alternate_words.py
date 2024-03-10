class Solution:

    def reverseAlternate(self, Str):
        
        lst=Str.split()
        for i in range(1,len(lst), 2):
            lst[i]=lst[i][::-1]
        
        return ' '.join(lst)