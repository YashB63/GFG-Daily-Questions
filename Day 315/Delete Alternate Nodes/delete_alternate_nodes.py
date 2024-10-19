class Solution:
    def deleteAlt(self, head):
        if head is None or head.next is None:
            return head
        
        current = head
        
        while current and current.next:
            
            next_node = current.next
            current.next = next_node.next  
            current = current.next  
            
        return head  
