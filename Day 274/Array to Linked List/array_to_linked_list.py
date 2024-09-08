class Solution:
    def constructLL(self, arr):
        if not arr:
            return None
            
        head = Node(arr[0])
        temp = head
        for i in arr[1:]:
            temp.next = Node(i)
            temp=temp.next
        return head