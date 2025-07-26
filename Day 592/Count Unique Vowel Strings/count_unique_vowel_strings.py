class Solution:
    def fact(self, n):
        res = 1
        for i in range(1, n + 1):
            res *= i
        return res

    def vowelCount(self, s):
        freq = {}
        vowels = 'aeiou'

        for c in s:
            if c in vowels:
                freq[c] = freq.get(c, 0) + 1

        if not freq:
            return 0

        choices = 1
        for count in freq.values():
            choices *= count

        dist = len(freq)
        res = choices * self.fact(dist)
        return res