class Solution:
    def countTriplets(self, head, x):
        ptr = head
        ptr1 = head
        ptr2 = head
        count = 0

        um = {}

        current = head
        while current is not None:
            um[current.data] = current
            current = current.next

        ptr1 = head
        while ptr1 is not None:
            ptr2 = ptr1.next
            while ptr2 is not None:
                p_sum = ptr1.data + ptr2.data

                if (x - p_sum) in um and um[x - p_sum] != ptr1 and um[
                        x - p_sum] != ptr2:
                    
                    count += 1

                ptr2 = ptr2.next
            ptr1 = ptr1.next

        return count // 3