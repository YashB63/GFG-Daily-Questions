class Solution:
    def reverse(self, head):
        if head is None or head.next == head:
            return head

        curr = head
        prev = None

        while True:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            if curr == head:
                break

        curr.next = prev
        return prev
        
        
    def deleteNode(self, head, key):
        if head is None or (head.next == head and head.data == key):
            return None

        if head.data == key:
            head.data = head.next.data
            head.next = head.next.next
            return head

        ptr = head.next
        prev = head

        while ptr != head:
            if ptr.data == key:
                prev.next = ptr.next
                return head

            prev = ptr
            ptr = ptr.next

        return head