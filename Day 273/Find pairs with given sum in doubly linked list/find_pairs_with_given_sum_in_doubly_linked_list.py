class Solution:
    def findPairsWithGivenSum(self, target : int, head : Optional['Node']) -> List[List[int]]:
        result = []
        right = head
        while right and right.next:
            right = right.next
        
        left = head
        while left.data < right.data:
            total = left.data + right.data
            if total == target:
                result.append([left.data, right.data])
                left = left.next
                right = right.prev
            elif total > target:
                right = right.prev
            else:
                left = left.next
        return result