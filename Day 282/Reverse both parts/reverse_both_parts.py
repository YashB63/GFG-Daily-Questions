class Solution:
    def reverse(self, head : Optional['Node'], k : int) -> Optional['Node']:
        l=[]
        while head is not None:
            l.append(head.data)
            head=head.next
        l=l[:k][::-1]+l[k::][::-1]
        for i in range(len(l)):
            l[i]=Node(l[i])
        for i in range(len(l)-1):
            l[i].next=l[i+1]
        return l[0]