class Solution:
    def totalElements(self, arr):
        from collections import defaultdict

        n = len(arr)
        if n == 0:
            return 0

        left = 0
        max_len = 0
        freq = defaultdict(int)  

        for right in range(n):
            freq[arr[right]] += 1

            while len(freq) > 2:
                freq[arr[left]] -= 1
                if freq[arr[left]] == 0:
                    del freq[arr[left]]
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len