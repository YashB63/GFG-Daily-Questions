import heapq

class Solution:
    def kSmallestPair(self, arr1, arr2, k):
        ans = []
        n1, n2 = len(arr1), len(arr2)
        if n1 == 0 or n2 == 0 or k <= 0:
            return ans

        heap = []
    
        for i in range(min(n1, k)):
            heapq.heappush(heap, (arr1[i] + arr2[0], i, 0))

        while heap and k > 0:
            _, i, j = heapq.heappop(heap)
            ans.append([arr1[i], arr2[j]])
            k -= 1
            
            if j + 1 < n2:
                heapq.heappush(heap, (arr1[i] + arr2[j + 1], i, j + 1))

        return ans
