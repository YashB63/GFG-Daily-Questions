class Solution:
    def modularNode(self, head, k):
        if k <= 0 or head is None:
            return -1
        i = 1
        modular_node = None

        temp = head
        while temp:
            if i % k == 0:
                modular_node = temp
            i += 1
            temp = temp.next

        if modular_node is None:
            return -1
        return modular_node.data