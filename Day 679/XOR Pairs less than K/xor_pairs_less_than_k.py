class TrieNode:
    def __init__(self):
        self.child = [None, None]
        self.count = 0

class Solution:
    def cntPairs(self, arr, k):
        MAX_BITS = 16 

        def insert(root, num):
            node = root
            for i in range(MAX_BITS - 1, -1, -1):
                bit = (num >> i) & 1
                if not node.child[bit]:
                    node.child[bit] = TrieNode()
                node = node.child[bit]
                node.count += 1

        def query(root, num, k):
            node = root
            ans = 0
            for i in range(MAX_BITS - 1, -1, -1):
                if not node:
                    break

                bitNum = (num >> i) & 1
                bitK = (k >> i) & 1

                if bitK == 1:
                    if node.child[bitNum]:
                        ans += node.child[bitNum].count
                    node = node.child[1 - bitNum]
                else:
                    node = node.child[bitNum]

            return ans

        root = TrieNode()
        count = 0

        for x in arr:
            count += query(root, x, k)
            insert(root, x)

        return count