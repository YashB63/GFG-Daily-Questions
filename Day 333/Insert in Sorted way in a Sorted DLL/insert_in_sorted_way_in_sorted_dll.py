class Solution:
    def sortedInsert(self, head, x):
        new_node = Node(x)
        
        if head is None or x < head.data:
            new_node.next = head
            if head:
                head.prev = new_node
            return new_node
        
        current = head
        while current.next and current.next.data < x:
            current = current.next
        
        new_node.next = current.next
        if current.next:
            current.next.prev = new_node
        current.next = new_node
        new_node.prev = current
        
        return head