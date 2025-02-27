import heapq

class Solution:
    def getMedian(self, arr):
        res,a,b=[],[],[]
        for i in arr:
            i=heapq.heappushpop(a,i)
            i=-heapq.heappushpop(b,-i)
            if len(a)==len(b):
                res.append(i)
                heapq.heappush(a,i)
            elif len(a)>len(b):
                res.append((a[0]+i)/2)
                heapq.heappush(b,-i)
            else:
                res.append((-b[0]+i)/2)
                heapq.heappush(a,i)
        return res