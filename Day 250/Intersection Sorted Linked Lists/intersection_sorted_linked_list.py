class Solution:
    def findIntersection(self,head1,head2):
        inter = linkedList()
        node1 = head1
        node2 = head2
        while node1 and node2:
            if node1.data == node2.data:
                inter.insert(node2.data)
                node1= node1.next
                node2= node2.next
                
            elif node1.data < node2.data:
                node1 = node1.next
            else:
                node2 = node2.next
        return inter.head