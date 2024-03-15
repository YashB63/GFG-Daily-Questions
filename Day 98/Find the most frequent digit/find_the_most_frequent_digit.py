class Solution:

    def solve(self, N):
        
        from collections import Counter
        digit_counts=Counter(N)
        most_frequent_digit = max([int(digit) for digit, count in digit_counts.items() if count == max(digit_counts.values())])
        return most_frequent_digit
