class Solution:

    def mostBooked(self, n, meetings):
        cnt = [0] * n  
        occ = []
        avail = list(range(n))
        heapq.heapify(avail)

        meetings.sort()

        for m in meetings:
            s, e = m

            while occ and occ[0][0] <= s:
                end_time, room = heapq.heappop(occ)
                heapq.heappush(avail, room)

            if avail:
                r = heapq.heappop(avail)
                heapq.heappush(occ, (e, r))
                cnt[r] += 1
            else:
                t, r = heapq.heappop(occ)
                heapq.heappush(occ, (t + (e - s), r))
                cnt[r] += 1

        maxCnt = 0
        res = 0
        for i in range(n):
            if cnt[i] > maxCnt:
                maxCnt = cnt[i]
                res = i

        return res