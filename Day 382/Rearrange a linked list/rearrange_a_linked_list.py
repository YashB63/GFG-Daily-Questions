class Solution:    
    def rearrangeEvenOdd(self, head):
        if head==None or head.next==None:
            return head
        p=head
        q=head.next
        np=p
        nq=q
        while nq!=None and nq.next!=None :
            np.next=np.next.next
            np=np.next
            nq.next=nq.next.next
            nq=nq.next
        np.next=q
        return head