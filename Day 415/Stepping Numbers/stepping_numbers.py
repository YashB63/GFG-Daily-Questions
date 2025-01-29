from collections import deque

class Solution:
    def steppingNumbers(self, n, m):
        q = deque(range(1, 10))
        count = 0
        if n == 0 and m == 0:
            return 1
        if n == 0:
            count += 1
        
        current_num = n
        while q:
            current_num = q.popleft()
            
            if n <= current_num <= m:
                count += 1
            if current_num > m:
                continue
                
            last_digit = current_num % 10
            if last_digit < 9:
                next_num = current_num * 10 + (last_digit + 1)
                q.append(next_num)
            if last_digit > 0:
                next_num = current_num * 10 + (last_digit - 1)
                q.append(next_num)
        return count