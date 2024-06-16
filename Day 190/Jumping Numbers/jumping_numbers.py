from collections import deque

class Solution:
    def jumpingNums(self, n):
        
        if n <= 9:
            return n
        
        result = 0
        queue = deque(range(1, 10))
        
        while queue:
            num = queue.popleft()
            if num <= n:
                result = max(result, num)
                last_digit = num % 10
                
                
                if last_digit == 0:
                    queue.append(num * 10 + last_digit + 1)
                
                elif last_digit == 9:
                    queue.append(num * 10 + last_digit - 1)
                else:
                    queue.append(num * 10 + last_digit - 1)
                    queue.append(num * 10 + last_digit + 1)
        
        return result