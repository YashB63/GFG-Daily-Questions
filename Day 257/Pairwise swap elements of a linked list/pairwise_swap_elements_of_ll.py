class Solution:    
    def pairWiseSwap(self, head):
        
        if not head or not head.next:
            return head
        
        dummy = Node(0)
        dummy.next = head
        prev = dummy
        curr = head
        
        while curr and curr.next:
            first = curr
            second = curr.next
          
            prev.next = second
            first.next = second.next
            second.next = first
            
            prev = first
            curr = first.next
        
        return dummy.next