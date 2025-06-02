class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def sortedInsert(self, head, data):
        new_node = Node(data)

        if head is None:
            new_node.next = new_node
            return new_node

        curr = head
        next_to_curr = head.next

        if data <= head.data:
            last_node = head
            while last_node.next != head:
                last_node = last_node.next
            new_node.next = head
            last_node.next = new_node
            return new_node

        while curr.next != head:
            if curr.data < data and next_to_curr.data >= data:
                new_node.next = curr.next
                curr.next = new_node
                return head
            else:
                curr = curr.next
                next_to_curr = next_to_curr.next

        new_node.next = head
        curr.next = new_node
        return head