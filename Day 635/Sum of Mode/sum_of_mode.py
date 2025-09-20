from typing import List
from collections import defaultdict
import heapq

class Solution:
    def sumOfModes(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if k <= 0 or k > n:
            return 0

        freq = defaultdict(int)

        heap = []

        for i in range(k):
            freq[arr[i]] += 1

        for v, f in freq.items():
            heapq.heappush(heap, (-f, v))

        def clean_top():
            while heap and -heap[0][0] != freq.get(heap[0][1], 0):
                heapq.heappop(heap)

        clean_top()
        total = heap[0][1]  

        for i in range(k, n):
            out_v = arr[i - k]
            in_v = arr[i]

            if out_v != in_v:
                old_f = freq[out_v]
                if old_f > 0:
                    freq[out_v] = old_f - 1
                    if freq[out_v] > 0:
                        heapq.heappush(heap, (-freq[out_v], out_v))
                    else:
                        del freq[out_v]  

                new_f = freq[in_v] + 1
                freq[in_v] = new_f
                heapq.heappush(heap, (-new_f, in_v))

            clean_top()
            total += heap[0][1]

        return total