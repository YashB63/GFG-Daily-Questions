class Solution:
    def sumOfLastN_Nodes(self, head, n):
        temp = head
        
        while n:
            temp = temp.next
            n -= 1
        
        temp2 = head
        
        while temp:
            temp = temp.next
            temp2 = temp2.next
        
        s = 0
        
        while temp2:
            s += temp2.data
            temp2 = temp2.next
        
        return s