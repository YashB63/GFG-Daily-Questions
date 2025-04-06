class Solution:
    def reverse(self,slow):
        prev=None
        current=slow.next
        while(current):
            front=current.next
            current.next=prev
            prev=current
            current=front
        return prev
        
    def modify_the_list(self, head):
        if(head is None or head.next is None):
            return head
        slow,fast=head,head.next
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
        slow.next=self.reverse(slow)
        current=slow.next
        fast=head
        while(current):
            val=current.data-fast.data
            current.data=fast.data
            fast.data=val
            fast=fast.next
            current=current.next
        slow.next=self.reverse(slow)   
        return head