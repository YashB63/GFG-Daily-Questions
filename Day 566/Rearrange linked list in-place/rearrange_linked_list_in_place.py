class Solution:
    def inPlace(self, root):
        slow = root
        fast = root.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        head1 = root
        head2 = slow.next
        slow.next = None

        prev = None
        cur = head2

        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        head2 = prev

        dummy = Node(0)
        temp = dummy
        while head1 or head2:
            if head1:
                temp.next = head1
                temp = temp.next
                head1 = head1.next
            if head2:
                temp.next = head2
                temp = temp.next
                head2 = head2.next

        return dummy.next