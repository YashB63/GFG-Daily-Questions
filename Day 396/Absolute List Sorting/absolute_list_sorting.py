class Node:

    def __init__(self, data):  
        self.data = data
        self.next = None


class Solution:
    def sortList(self, head):
        prev = head
        curr = head.next
        while curr != None:
            if curr.data < 0:
                prev.next = curr.next
                curr.next = head
                head = curr
                curr = prev
            else:
                prev = curr
            curr = curr.next
        return head