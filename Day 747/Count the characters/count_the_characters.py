class Solution:
    def getCount(self, S, N):
        char_count = {}

        previous_char = None

        for char in S:
            if char != previous_char:
                if char not in char_count:
                    char_count[char] = 1
                else:
                    char_count[char] += 1
            previous_char = char

        count = sum(1 for value in char_count.values() if value == N)
        
        return count