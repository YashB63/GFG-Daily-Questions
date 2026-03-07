class Solution:
    def intersectPoint(self, head1, head2):
        n1 = n2 = 0
        temp = head1
        while temp:
            n1 += 1
            temp = temp.next

        temp = head2
        while temp:
            n2 += 1
            temp = temp.next

        while n1 > n2:
            head1 = head1.next
            n1 -= 1

        while n2 > n1:
            head2 = head2.next
            n2 -= 1

        while head1 and head2 and head1 != head2:
            head1 = head1.next
            head2 = head2.next

        return head1