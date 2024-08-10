class Solution:
    def findMid(self, head):
        n = 0
        temp = head
        while(temp):
            n += 1
            temp = temp.next
        if n == 1:
            return head.data
        i = 0
        mid = n//2
        temp=head
        while(temp):
            if i == mid:
                return temp.data
            i += 1
            temp = temp.next