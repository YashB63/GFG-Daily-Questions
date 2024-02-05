import string

class Solution:
    
    def checkPangram(self,s):
        
        x = set(string.ascii_lowercase)
        
        return set(s.lower()) >= x