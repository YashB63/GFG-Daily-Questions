class Solution:
    def delete_node(self, head, n):
        
        if n == 1:
            nxt = head.next
            head.next = None
            nxt.prev = None
            return nxt
          
        temp = head  
        while n != 1:
            temp = temp.next
            n -= 1
            
        temp.prev.next = temp.next
        if temp.next:
            temp.next.prev = temp.next
            
        return head