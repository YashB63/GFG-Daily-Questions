class Solution:
    def detectLoop(self, head):
        st = set()
        while head is not None:
            if head in st:
                return True
            st.add(head)
            head = head.next
        return False