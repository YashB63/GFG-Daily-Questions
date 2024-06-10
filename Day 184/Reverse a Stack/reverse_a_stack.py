from typing import List

class Solution:
    def reverse(self,St): 
        
        lft = 0
        rgt = len(St)-1
        while lft <rgt:
            
            St[lft],St[rgt] = St[rgt],St[lft]
            lft += 1
            rgt -= 1