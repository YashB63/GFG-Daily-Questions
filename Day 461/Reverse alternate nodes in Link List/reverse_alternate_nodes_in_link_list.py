class Solution:
    def reverseList(self,head):
        prev=None
        cur=head
        while cur is not None:
            next_node=cur.next
            cur.next=prev
            prev=cur
            cur=next_node
        return prev
        
    def rearrange(self, head):
        if head is None or head.next is None:
            return head
        
        temp1=head
        temp2=head.next
        temp=head.next
        
        while temp1 and temp2 and temp2.next:
            temp1.next=temp1.next.next
            temp2.next=temp2.next.next
            temp1=temp1.next
            temp2=temp2.next
        
        temp1.next=self.reverseList(temp)
        return head
