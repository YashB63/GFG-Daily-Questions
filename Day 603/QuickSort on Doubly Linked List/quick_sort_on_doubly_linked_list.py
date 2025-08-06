class Solution:
    def get_tail(self, cur):
        while cur is not None and cur.next is not None:
            cur = cur.next
        return cur

    def partition(self, head, end):
        pivot = end
        prev = None
        cur = head
        tail = pivot
        new_head = None
        new_end = None

        while cur != pivot:
            if cur.data < pivot.data:
                if new_head is None:
                    new_head = cur
                prev = cur
                cur = cur.next
            else:
                if prev:
                    prev.next = cur.next
                if cur.next:
                    cur.next.prev = prev
                tmp = cur.next
                cur.next = None
                tail.next = cur
                cur.prev = tail
                tail = cur
                cur = tmp

        if new_head is None:
            new_head = pivot

        new_end = tail

        return pivot, new_head, new_end

    def quick_sort_recur(self, head, end):
        if not head or head == end:
            return head

        pivot, new_head, new_end = self.partition(head, end)

        if new_head != pivot:
            tmp = new_head
            while tmp.next != pivot:
                tmp = tmp.next
            tmp.next = None
            pivot.prev = None

            new_head = self.quick_sort_recur(new_head, tmp)

            tmp = self.get_tail(new_head)
            tmp.next = pivot
            pivot.prev = tmp

        pivot.next = self.quick_sort_recur(pivot.next, new_end)
        if pivot.next:
            pivot.next.prev = pivot

        return new_head

    def quick_sort(self, head):
        tail = self.get_tail(head)
        return self.quick_sort_recur(head, tail)