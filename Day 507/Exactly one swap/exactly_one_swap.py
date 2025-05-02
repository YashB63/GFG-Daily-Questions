from collections import Counter

class Solution:
    def countStrings(self, S): 
        n = len(S)
        total_swaps = (n * (n - 1)) // 2  

        freq = Counter(S)

        same_char_swaps = 0
        for count in freq.values():
            if count > 1:
                same_char_swaps += (count * (count - 1)) // 2

        distinct = total_swaps - same_char_swaps

        if same_char_swaps > 0:
            distinct += 1  

        return distinct