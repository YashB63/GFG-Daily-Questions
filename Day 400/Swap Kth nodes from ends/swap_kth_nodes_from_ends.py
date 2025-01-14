class Solution:
    def swap_kth_node(self, head, k):
        if head is None or head.next is None: return head
        
        n = len(before)
        i1, i2 = k - 1, n - k
        if i1 < 0 or i2 < 0: return head
        result = None
        for i in reversed(range(n)):
            node = before[i1 if i == i2 else i2 if i == i1 else i]
            node.next = result
            result = node
        return result