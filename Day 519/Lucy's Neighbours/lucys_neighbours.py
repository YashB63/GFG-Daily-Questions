class Solution:
    def Kclosest(self, arr, n, x, k):
        max_heap = [ ( -1*abs(x-arr[i]) , -1*arr[i] ) for i in range(k) ]
        heapq.heapify(max_heap)
        
        for i in range(k,n):
            dist = -1*max_heap[0][0]
            hno  = -1*max_heap[0][1]
            if abs(arr[i]-x)<dist or ( abs(arr[i]-x)==dist and arr[i]<hno ):
                heapq.heappop(max_heap)
                heapq.heappush( max_heap, ( -1*abs(x-arr[i]) , -1*arr[i] ) )
        
        ret=[ -1*x[1] for x in max_heap]
        ret.sort()
        return ret