import heapq
from collections import defaultdict

class Solution :
    def rearrangeString(self, str):
        freq = defaultdict(int)
        for i in str:
            freq[i]+=1
            
        freq = sorted(freq.items(), key=lambda x: -x[1])
        
        heap = [(-f, char) for char, f in freq]
        heapq.heapify(heap) 

        prev=None
        res = ""
        while heap or prev:
            if not heap and prev:
                return ""
            if heap:
                f, char = heapq.heappop(heap)
                res+=char
                f+=1
                if f!=0:
                    if prev:
                        heapq.heappush(heap, prev)
                    prev = (f, char)

                else:
                    if prev:
                        heapq.heappush(heap, prev)
                        prev=None
        return res