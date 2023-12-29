from typing import List

class Solution:
    
    def sumZero(self, temp, starti, endj, n):
        presum = {}
        s = 0
        max_len = 0
        for i in range(n):
            s += temp[i]
            
            if temp[i] == 0 and max_len == 0:
                starti[0] = i
                endj[0] = i
                max_len = 1
                
            if s == 0:
                if max_len < i + 1:
                    starti[0] = 0
                    endj[0] = i
                max_len = i + 1
                
            if s in presum:
                prev = max_len
                max_len = max(max_len, i - presum[s])
                if prev < max_len:
                    endj[0] = i
                    starti[0] = presum[s] + 1
            else:
                presum[s] = i
                
        return max_len != 0
    
    def sumZeroMatrix(self, a : List[List[int]]) -> List[List[int]]:
        
        r = len(a)
        c = len(a[0])
        temp = [0] * r
        
        s_up = 0
        s_down = 0
        s_left = 0
        s_right = 0
        maxl = float('-inf')
        
        for left in range(c):
            temp = [0] * r
            for right in range(left, c):
                for i in range(r):
                    temp[i] += a[i][right]
                    
                starti = [0]
                endj = [0]
                is_sum = self.sumZero(temp, starti, endj, r)
                ele = (endj[0] - starti[0] + 1) * (right - left + 1)
                
                if is_sum and ele > maxl:
                    s_up = starti[0]
                    s_down = endj[0]
                    s_left = left
                    s_right = right
                    maxl = ele
                    
        res = []
        
        if s_up ==s_down == s_left == s_right == 0 and a[0][0] != 0:
            return res
            
        for j in range(s_up, s_down + 1):
            count = []
            for i in range(s_left, s_right + 1):
                count.append(a[j][i])
            res.append(count)
            
        return res