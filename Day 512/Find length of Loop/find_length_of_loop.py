class Solution:
    def countNodesInLoop(self, head):
        fast,slow = head,head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                count = 1
                fast = fast.next
                while fast!=slow:
                    count+=1
                    fast = fast.next
                return count
        return 0