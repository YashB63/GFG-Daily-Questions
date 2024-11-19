def intersetPoint(head1,head2):
    def length(head):
        n=0
        while head is not None:
            n+=1
            head=head.next
        return n
    l1=length(head1)
    l2=length(head2)
    while(l1>l2):
        head1=head1.next
        l1-=1
    while(l2>l1):
        head2=head2.next
        l2-=1
    while(head1 is not None and head1!=head2):
        head1=head1.next
        head2=head2.next
    return head1.data if head1 is not None else -1