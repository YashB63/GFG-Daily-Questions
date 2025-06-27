from collections import Counter

class Solution:
    def validgroup(self, arr, k):
        if len(arr) % k != 0:
            return False

        count = Counter(arr)
        sorted_keys = sorted(count)

        for num in sorted_keys:
            while count[num] > 0:
                for i in range(k):
                    if count[num + i] == 0:
                        return False
                    count[num + i] -= 1
        return True