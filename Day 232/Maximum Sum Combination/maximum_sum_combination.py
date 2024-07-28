import heapq

class Solution:
    def maxCombinations(self, N, K, A, B):
        A.sort(reverse = True)
        B.sort(reverse = True)
        minHeap = []
        
        for i in range(N):
            for j in range(N):
                sum_comb = A[i] + B[j]
                if len(minHeap) < K:
                    heapq.heappush(minHeap, sum_comb)
                else:
                    if sum_comb > minHeap[0]:
                        heapq.heapreplace(minHeap, sum_comb)
                    else:
                        break
        
        minHeap.sort(reverse = True)
        return minHeap