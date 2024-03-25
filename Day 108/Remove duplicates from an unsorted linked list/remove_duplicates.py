class Solution:
    
    def removeDuplicates(self, head):
       
        if not head or not head.next:
            return head
            
        h = {}
        prev = head
        curr= head.next
        h[prev.data] = 1
        while curr:
            if curr and curr.data in h:
                prev.next = curr.next
                curr = prev.next
            
            else:
                if curr:
                    h[curr.data] = 1
                    prev = prev.next
                    curr = curr.next
            
        return head