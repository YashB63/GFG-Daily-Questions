class Solution:
    
    def reverseList(self, head):
        
        if head == None or head.next == None:
            return head
        top = None
        while head:
            newnode = Node(head.data)
            newnode.next = top
            top = newnode
            head = head.next
        return top