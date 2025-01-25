class Solution:
    def add_polynomial(self, head1, head2):
        dummy = Node(0, 0)
        curr = dummy
        
        while curr:
            if head1 == None:
                curr.next = head2
                break
                
            elif head2 == None:
                curr.next = head1
                break
            
            elif head1.power > head2.power:
                curr.next = Node(head1.coef, head1.power)
                head1 = head1.next
            
            elif head1.power < head2.power:
                curr.next = Node(head2.coef, head2.power)
                head2 = head2.next
            
            elif head1.power == head2.power:
                curr.next = Node(head1.coef + head2.coef, head1.power)
                head1 = head1.next
                head2 = head2.next
            curr = curr.next
        return dummy.next