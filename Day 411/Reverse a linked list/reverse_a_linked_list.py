class Solution:
    def reverseList(self, head):
        temp = head
        prev = None
        while temp:
            
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev