class Solution:
    def divide(self, head):
        dummy = node()
        dummy.data = 0
        dummy.next = head
        temp1, temp2 = dummy, dummy

        while temp2.next and temp2.next.data % 2 == 0:
            temp2 = temp2.next

        temp1 = temp2

        while temp2.next:
            if temp2.next.data % 2 == 0:
                h = temp2.next
                temp2.next = temp2.next.next
                h.next = temp1.next
                temp1.next = h
                temp1 = temp1.next
            else:
                temp2 = temp2.next

        return dummy.next