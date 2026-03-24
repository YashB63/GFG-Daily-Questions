class Solution:
    def isSorted(self, head):
        ascending = desceding = True
        
        while head.next:
            ascending = ascending and head.data<=head.next.data
            desceding = desceding and head.data>=head.next.data
            head = head.next
        
        return ascending or desceding