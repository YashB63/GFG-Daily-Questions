class Solution:
    def countPair(self, head1, head2, n1, n2, x):
        
        count = 0
       
        values = {}
        while head2:
            values[head2.data] = values.get(head2.data, 0) + 1
            head2 = head2.next
            
        
        while head1:
            if (x - head1.data) in values:
                count += values[x - head1.data]
            head1 = head1.next
        
        return count