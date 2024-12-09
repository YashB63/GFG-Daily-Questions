import heapq

class Solution:
    def isStraightHand(self, N, groupSize, hand):
        cnt={}
        for i in hand:
            if i not in cnt:
                cnt[i]=1
            else:
                cnt[i]+=1
        l=list(cnt.keys())
        heapq.heapify(l)
        while l:
            i=heapq.heappop(l)
            if cnt[i]>0:
                c=cnt[i]
                for j in range(i,i+groupSize):
                    if j not in cnt or cnt[j]<c:
                        return False
                    cnt[j]-=c
            if cnt[i]<0:
                return False
        return True