class Solution():
    def rotateDLL(self, start, p):
        temp=start
        for i in range(p-1):
            temp=temp.next
        newhead=temp.next
        temp.next=None
        temp1=newhead
        while temp1.next:
            temp1=temp1.next
        temp1.next=start
        return newhead