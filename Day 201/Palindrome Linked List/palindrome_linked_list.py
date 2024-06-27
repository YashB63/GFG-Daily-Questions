class Solution:
    def reverse(self,head):
        nex = head
        curr = head
        prev = None
        
        while nex:
            nex = nex.next
            curr.next = prev
            prev = curr
            curr = nex
        
        return prev
        
    def findmid(self,head):
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
        
    def isPalindrome(self, head):
        
        if head is None and head.next is None:
            return True
        
        mid = self.findmid(head)
        last = self.reverse(mid)
        
        while last is not None:
            if head.data != last.data :
                return False
            head = head.next
            last = last.next
        
        return True