class Solution:
    def isPossible(self, S, N, X, A):
        sum_l = [S]
        current_sum = S
        
        for i in A:
            value = current_sum + i
            sum_l.append(value)
            current_sum += sum_l[-1]
            if current_sum >= X:
                break
        
        for num in reversed(sum_l):
            if X == 0:
                return 1
            if num <= X:
                X -= num
        return 1 if X == 0 else 0