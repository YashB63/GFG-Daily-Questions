class Solution:
    def deleteAlt(self, head):
        temp=head
        while temp and temp.next is not None:
            temp.next=temp.next.next
            temp=temp.next
        return head