import heapq

class Compare:
    def __init__(self,node):
        self.node=node
    
    def __lt__(self,other):
        return self.node.data<other.node.data
        
class Solution:
    def mergeKLists(self,arr,K):
        pq=[]
        for head in arr:
            heapq.heappush(pq,Compare(head))
        
        head=Node(-1)
        tail=head
        while pq:
            node=heapq.heappop(pq).node
            if node.next:
                heapq.heappush(pq,Compare(node.next))
            
            tail.next=node
            tail=tail.next
            tail.next=None
            
        return head.next