class Solution:
    def addOne(self,head):
        s=''
        curr=head
        while curr!=None:
            s=s+str(curr.data)
            curr=curr.next
        v=Node(int(s)+1)
        return v