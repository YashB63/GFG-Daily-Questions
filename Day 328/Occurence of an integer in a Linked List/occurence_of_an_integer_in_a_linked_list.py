class Solution:
    def count(self, head, key):
        cur = head
        ans = 0
        while cur:
            if cur.data == key:
                ans += 1
            cur = cur.next
        return ans