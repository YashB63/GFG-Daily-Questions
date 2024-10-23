class Solution:
    def alternatingSplitList(self, head):
        o_head1 = Node(0)
        o_head2 = Node(0)
        head1 = o_head1
        head2 = o_head2
        odd = True
        while head:
            if odd:
                head1.next = head
                head = head.next
                head1 = head1.next
                head1.next = None
            else:
                head2.next = head
                head = head.next
                head2 = head2.next
                head2.next = None
            odd ^= True
        return [o_head1.next, o_head2.next]