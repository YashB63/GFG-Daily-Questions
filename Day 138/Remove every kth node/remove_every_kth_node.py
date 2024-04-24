class Solution:
    def deleteK(self, head, k):
        
        if k==1:
            return None
        
        temp = head
        prev = None
        while temp:
            skip = k-1
            while skip and temp:
                prev = temp
                temp = temp.next
                skip -= 1
            
            if temp:
                prev.next = temp.next
            temp = prev.next
        
        return head