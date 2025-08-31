class Solution:
    def insertAtPos(self, head, p, x):
        temp = head

        while p != 0:
            temp = temp.next
            p -= 1

        n = Node(x)

        if temp.next is None:
            n.prev = temp
            temp.next = n
        else:
            n.next = temp.next
            temp.next = n
            temp.next.prev = n
            n.prev = temp

        return head