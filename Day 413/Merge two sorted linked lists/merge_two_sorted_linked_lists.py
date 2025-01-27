class Solution:
    def sortedMerge(self,head1, head2):
        res=None
        if head1.data<=head2.data:
            res=Node(head1.data)
            head1=head1.next
        else:
            res=Node(head2.data)
            head2=head2.next
        head=res
        while head1 and head2:
            if head1.data<=head2.data:
                res.next=Node(head1.data)
                head1=head1.next
            else:
                res.next=Node(head2.data)
                head2=head2.next
            res=res.next
        if head1 is None:
            res.next=head2
        if head2 is None:
            res.next=head1
        return head