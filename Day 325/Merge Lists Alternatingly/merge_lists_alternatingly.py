class Solution:
    def merge_list(self, head1, head2):
        curr1 = head1
        curr2 = head2
        while curr1 != None and curr2 != None:
            next1 = curr1.next
            next2 = curr2.next
            curr1.next = curr2
            curr2.next = next1
            curr1 = next1
            curr2 = next2
        return [head1, curr2]