class Solution:
    def deleteMid(self,head):
        
        if head is None or head.next is None:
            return None
        slow=head
        fast=head
        Dummy=Node(-1)
        temp=Dummy
        while fast!=None and fast.next!=None:
            Dummy.next=slow
            Dummy=slow
            slow=slow.next
            fast=fast.next.next
        Dummy.next=slow.next
        return temp.next