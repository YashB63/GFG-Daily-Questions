class Solution:
    def removeDuplicates(self, head):
        if not head or not head.next:
            return head
        curr = head
        while curr and curr.next:
            if curr.data == curr.next.data:
                curr.next = curr.next.next
                if curr.next:
                    curr.next.prev = curr
            else:
                curr = curr.next
                    
        return head