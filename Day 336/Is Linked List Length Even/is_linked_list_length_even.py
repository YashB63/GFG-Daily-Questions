class Solution:
    def isLengthEven(self, head):
        n=0
        while(head):
            n+=1
            head=head.next
        return n%2==0