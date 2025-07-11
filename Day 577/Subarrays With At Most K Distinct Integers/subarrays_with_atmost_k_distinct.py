class Solution:
    def countAtMostK(self, arr, k):
        n = len(arr)
        res = 0

        left, right = 0, 0

        freq = defaultdict(int)
        while right < n:
            freq[arr[right]] += 1

            if freq[arr[right]] == 1:
                k -= 1

            while k < 0:
                freq[arr[left]] -= 1
                if freq[arr[left]] == 0:
                    k += 1
                left += 1

            res += (right - left + 1)
            right += 1
        return res