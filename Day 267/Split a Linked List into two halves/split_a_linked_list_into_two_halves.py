class Solution:
    def splitList(self, head):
        temp=head
        ptr=head
        l=1
        while ptr.next!=head:
            ptr=ptr.next
            l+=1
        if l%2==0:
            k=(l//2)
        else:
            k=(l//2)+1
        ptr1=head
        ptr2=head
        c=0
        while c<k-1:
            ptr2=ptr2.next
            c+=1
        second_half=ptr2.next
        ptr2.next=head
        ptr.next=second_half
        return head,second_half