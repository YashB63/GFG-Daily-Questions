class Solution:
    def searchKey(self, n, head, key):
        while head:
            if head.data==key:
                return True
            head=head.next
        return False