class Solution:
    def insertAtEnd(self, head, x):
        temp = Node(x)
        if head is None:
            return temp
        else:
            ptr = head
            while ptr.next:
                ptr = ptr.next
            ptr.next = temp
        return head