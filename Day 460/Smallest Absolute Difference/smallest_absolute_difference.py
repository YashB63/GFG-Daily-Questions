import heapq

def kthDiff( a, n, k):
    out = []
    heapq.heapify(out)
    for i in range(n-1):
        for j in range(i+1, n):
            diff = abs(a[i]-a[j])
            heapq.heappush(out, diff)
    mn = heapq.nsmallest(k, out)
    return mn[-1]