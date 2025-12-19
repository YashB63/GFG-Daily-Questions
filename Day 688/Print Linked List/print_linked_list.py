class Solution:
    def printList(self, head):
        result = []
        while head is not None:
            result.append(head.data)
            head = head.next
            
        return result