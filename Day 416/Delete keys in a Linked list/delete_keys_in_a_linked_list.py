class Solution:
    def deleteAllOccurances(self,head,x):
        prev = None
        curr = head
        while(curr!=None):
            if(head.data==x and curr==head):
                head = head.next
                curr = head
                
            elif(curr.data==x):
                prev.next = curr.next
                curr = curr.next
            else:   
                prev = curr
                curr = curr.next
                
        return head