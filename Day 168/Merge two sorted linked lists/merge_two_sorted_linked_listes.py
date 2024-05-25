class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
def sortedMerge(head1, head2):
    
    dummy = Node(0)
    current = dummy
    while head1 and head2:
        if head1.data<head2.data:
            current.next=head1
            head1=head1.next
        else:
            current.next=head2
            head2=head2.next
        current=current.next
        
    if head1:
        current.next=head1
    if head2:
        current.next=head2
    return dummy.next