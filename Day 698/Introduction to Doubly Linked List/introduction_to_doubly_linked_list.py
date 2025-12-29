class Solution:
    def constructDLL(self, arr):
        head=Node(arr[0])
        Node.prev=None
        Node.next=None
        curr=head
        for i in range(1,len(arr)):
            temp=Node(arr[i])
            temp.prev=curr
            temp.next=None
            curr.next=temp
            curr=temp
        return head