class Solution:
    def union(self, head1,head2):
    
        se=set()
        temp=head1
        while(temp):
            se.add(temp.data)
            temp=temp.next
        temp=head2
        while(temp):
            se.add(temp.data)
            temp=temp.next
        lst=list(se)
        lst.sort()
        head1=None
        head1=Node(lst[0])
        temp=head1
        for i in range(1,len(lst)):
            temp.next=Node(lst[i])
            temp=temp.next
        return head1