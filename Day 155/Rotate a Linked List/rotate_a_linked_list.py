class Solution:
    
    def rotate(self, head, k):
        
        length = 0
        curr = head
        tail = None
        while curr:
            tail = curr
            curr = curr.next
            length += 1
        count = k%n
        if count == 0:
            return head
        else:
            prev = None
            curr = head
            while count > 0:
                prev = curr
                curr = curr.next
                count -= 1
            tail.next = head
            prev.next = None
            return curr