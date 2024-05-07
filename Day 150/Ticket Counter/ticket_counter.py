class Solution:
    def distributeTicket(self, N : int, K : int) -> int:
        
        clock = True
        left = 1
        right = N
        while right-left>=K:
            if clock:
                left+=K
            else:
                right = right - K
            clock = not clock
        if clock:
            return right
        return left