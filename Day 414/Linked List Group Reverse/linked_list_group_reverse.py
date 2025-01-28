class Solution:
    def reverseKGroup(self, head, k):
        if not head or not head.next:
            return head
        
        prev=None
        temp=head
        cnt=0
        
        while temp and cnt<k:
            nxt=temp.next
            temp.next=prev
            prev=temp
            temp=nxt
            cnt+=1
        
        head.next=self.reverseKGroup(temp,k)
        
        return prev