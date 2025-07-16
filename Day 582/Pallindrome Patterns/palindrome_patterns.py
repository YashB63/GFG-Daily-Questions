from typing import List
from collections import Counter

class Solution:
    def is_palindrome(self, s: str) -> bool:
        freq = Counter(s)
        odd_count = sum(1 for val in freq.values() if val % 2 != 0)
        return odd_count <= 1

    def all_palindromes(self, s: str) -> List[str]:
        if not self.is_palindrome(s):
            return []

        freq = Counter(s)
        half = []
        middle = ''
        
        for char in sorted(freq):
            count = freq[char]
            if count % 2 == 1:
                middle = char
            half.extend([char] * (count // 2))
        
        res = set()
        def backtrack(path, used):
            if len(path) == len(half):
                half_str = ''.join(path)
                full_palindrome = half_str + middle + half_str[::-1]
                res.add(full_palindrome)
                return
            for i in range(len(half)):
                if used[i]:
                    continue
                if i > 0 and half[i] == half[i-1] and not used[i-1]:
                    continue
                used[i] = True
                path.append(half[i])
                backtrack(path, used)
                path.pop()
                used[i] = False

        half.sort()
        backtrack([], [False] * len(half))
        return sorted(res)