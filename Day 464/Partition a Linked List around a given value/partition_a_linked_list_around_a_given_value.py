class Solution:
    def partition(self, head, x):
        l1=[]
        l2=[]
        l3=[]
        while head:
            if head.data<x:
                l1.append(head.data)
                head=head.next
            elif head.data==x:
                l2.append(head.data)
                head=head.next
            else:
                l3.append(head.data)
                head=head.next
        result=l1+l2+l3
        for i in result:
            print(i,end=" ")