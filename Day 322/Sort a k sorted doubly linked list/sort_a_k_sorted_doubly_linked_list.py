class Solution:
    def sortAKSortedDLL(self, head, k):
        temp = k+1
        curr = head
        pq = []
        
        while temp:
            heapq.heappush(pq, curr.data)
            temp -= 1
            curr = curr.next
        
        newCurr = head
        while newCurr:
            val = heapq.heappop(pq)
            newCurr.data = val
            newCurr = newCurr.next
            
            if curr:
                heapq.heappush(pq, curr.data)
                curr = curr.next
        return head