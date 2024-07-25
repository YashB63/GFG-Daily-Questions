class Solution:
    
    def merging_list(self,l1,l2):
        dummy = Node(0)
        cur = dummy
        while l1 and l2:
            if l1.data < l2.data:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2

        return dummy.next
    def split_list(self,head):
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if prev:
            prev.next = None
        return head,slow
        
    def mergeSort(self, head):
        if not head or not head.next:
            return head
        
        left,right = self.split_list(head)
        
        left = self.mergeSort(left)
        right = self.mergeSort(right)
        
        return self.merging_list(left,right)