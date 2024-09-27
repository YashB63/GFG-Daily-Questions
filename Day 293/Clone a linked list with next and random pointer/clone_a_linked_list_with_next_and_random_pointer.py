class Solution:
    def copyList(self, head):
        new_head = prev = Node(-1)
        temp = head
        old_to_new = {}
        
        while temp:
            new_node = Node(temp.data)
            old_to_new[temp] = new_node
            
            prev.next = new_node
            prev = new_node
            temp = temp.next
        
        temp = head
        while temp:
            if temp.random:
                old_to_new[temp].random = old_to_new[temp.random]
            temp = temp.next
        
        return new_head.next