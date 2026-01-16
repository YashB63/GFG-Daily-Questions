class Solution:
    def find(self, head):
        if head.next == None:
            return 1
        return 1 + self.find(head.next)
    
    def generate(self, head1, head2, skip):
        if head1 == None and head2 == None:
            return None, 0
        val = head1.data
        if skip <= 0:
            val += head2.data
        node_next, rem = self.generate(
            head1.next,
            head2 if skip > 0 else head2.next,
            skip - 1
        )
        val += rem
        node = Node(val%10)
        node.next = node_next
        return node, val//10
        
    def addTwoLists(self, head1, head2):
        len_1 = self.find(head1)
        len_2 = self.find(head2)
        out = []
        if len_1 > len_2:
            out, car = self.generate(head1, head2, len_1 - len_2)
        else:
            out, car = self.generate(head2, head1, len_2 - len_1)
        if car:
            node = Node(car)
            node.next = out
            return node
        while out.data == 0:
            out = out.next
        return out