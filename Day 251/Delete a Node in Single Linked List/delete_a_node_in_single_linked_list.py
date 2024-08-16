def delNode(head, k):
    if k==1:
        return head.next
    i=1
    temp=head
    while(temp):
        if i==k-1:
            temp.next=temp.next.next
            break
        temp=temp.next
        i+=1
    return head