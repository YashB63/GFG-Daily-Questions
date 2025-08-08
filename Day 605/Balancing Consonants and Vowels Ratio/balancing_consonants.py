from collections import defaultdict

class Solution:
    def isVowel(self, ch):
        return ch in 'aeiou'

    def countBalanced(self, arr):
        n = len(arr)
        res = 0
        prefix = 0

        freq = defaultdict(int)

        freq[0] = 1

        for i in range(n):
            score = 0

            for ch in arr[i]:
                if self.isVowel(ch):
                    score += 1
                else:
                    score -= 1

            prefix += score

            res += freq[prefix]

            freq[prefix] += 1

        return res