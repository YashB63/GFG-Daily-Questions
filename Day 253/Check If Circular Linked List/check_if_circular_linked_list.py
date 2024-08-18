class Solution:
    def isCircular(self, head):
        curr=head
        while curr!=None and curr.next!=None:
            if curr!=head:
                curr=curr.next
            else:
                return "true"
        return "false"