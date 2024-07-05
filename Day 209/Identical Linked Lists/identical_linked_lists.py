def areIdentical(head1, head2):
    
    if head1 is None and head2 is None:
        return True
    if head1 is None or head2 is None:
        return False
    curr1=head1
    curr2=head2
    while curr1!=None and curr2!=None:
        if curr1.data==curr2.data:
            curr1=curr1.next
            curr2=curr2.next
        else:
            return False
    if curr1 is None and curr2 is None:
        return True
    
    return False