class Solution:
    
    def addTwoLists(self, num1, num2):
        
        n1 = 0
        n2 = 0
        temp = num1
        while temp:
            n1 = n1*10 + temp.data
            temp = temp.next
        temp = num2
            
        while temp:
            n2 = n2*10 + temp.data
            temp = temp.next
        nsum = n1 + n2
        stupid_head = Node(-1)
        temp = stupid_head
        
        
        for n in str(nsum):
            new_node = Node(int(n))
            temp.next = new_node
            temp = temp.next
        return stupid_head.next