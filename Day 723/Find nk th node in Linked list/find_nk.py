class Solution:
     def fractional_node(self, head, k):
        if head is None or k <= 0:
            return -1

        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
        
        from math import ceil
        fractional_index = ceil(count / k)

        current = head
        for _ in range(fractional_index - 1):
            if current is None:
                return -1  
            current = current.next

        return current.data if current else -1