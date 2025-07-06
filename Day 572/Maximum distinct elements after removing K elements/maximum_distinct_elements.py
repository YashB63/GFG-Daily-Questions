class Solution:
    def maxDistinctNum(self, arr, k):
        frequency_map = {}

        for num in arr:
            frequency_map[num] = frequency_map.get(num, 0) + 1

        max_heap = [-freq for freq in frequency_map.values()]
        heapq.heapify(max_heap)

        while k > 0 and max_heap:
            top_freq = -heapq.heappop(max_heap)
            top_freq -= 1
            k -= 1

            if top_freq > 0:
                heapq.heappush(max_heap, -top_freq)

        return len(max_heap)