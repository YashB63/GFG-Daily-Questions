import re

class Solution:
    def isPatternPresent(self, S , P):
        
        return int(not not re.search(P, S))
