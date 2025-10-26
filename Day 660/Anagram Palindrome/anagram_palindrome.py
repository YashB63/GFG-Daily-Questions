class Solution:
    def isPossible(self, S):
        freq = {}
        for ch in S:
            freq[ch] = freq.get(ch, 0) + 1

        odd_freq = 0
        for count in freq.values():
            if count % 2 != 0:
                odd_freq += 1
            if odd_freq > 1:
                return 0  

        return 1  