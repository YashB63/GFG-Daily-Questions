class Solution:
    def insertInMiddle(self, head, x):
        if not head: return Node(x)
        slow=head
        fast=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        node=Node(x)
        node.next=slow.next
        slow.next=node
        return head