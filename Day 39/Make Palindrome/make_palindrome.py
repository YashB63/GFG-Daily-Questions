from typing import List

class Solution:
    def makePalindrome(self, n : int, arr : List[str]) -> bool:
        
        x = []
        for i in arr:
            if i[::-1] in x:
                x.remove(i[::-1])
            else:
                x.append(i)
                
        if(len(x) == 1 and x[0] == x[0][::-1]):
            return True
            
        return True if len(x)==0 else False