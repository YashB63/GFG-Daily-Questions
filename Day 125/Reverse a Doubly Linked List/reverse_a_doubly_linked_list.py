class Solution:
    def reverseDLL(self, head):
        
        if head == None:
            return None
        if head.next == None:
            return head

        curr = head
        prev = None

        while curr != None:
            prev = curr
            curr.next, curr.prev = curr.prev, curr.next
            curr = curr.prev

        return prev