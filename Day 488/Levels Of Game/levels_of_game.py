from typing import List

class Solution:
    def maxLevel(self, h:int,m:int) -> int:
        level = 0
        roads = [(-20, 5), (-5, -10), (3, 2)]
        while True:
            if level % 2 == 0: # r3
                h += roads[2][0]
                m += roads[2][1]
                level += 1
                continue
            
            if h < 6:
                break
            
            if h < 21 and m < 11:
                break
            
            if m >= 10: 
                h += roads[1][0]
                m += roads[1][1]
            else: 
                h += roads[0][0]
                m += roads[0][1]
                
            level += 1

        return level