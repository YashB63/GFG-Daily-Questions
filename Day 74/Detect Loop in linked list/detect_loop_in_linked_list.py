class Solution:
    
    def detectLoop(self, head):
        
        fast = head
        while fast and fast.next:
            head = head.next
            fast = fast.next.next
            if head is fast:
                return True
        return False