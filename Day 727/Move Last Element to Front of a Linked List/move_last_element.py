from typing import Optional

class Solution:
    def moveToFront(self, head : Optional['Node']) -> Optional['Node']:
        prev = None
        curr =head
        while curr.next!=None:
            prev = curr
            curr = curr.next
        prev.next = None
        curr.next = head
        return curr    
        