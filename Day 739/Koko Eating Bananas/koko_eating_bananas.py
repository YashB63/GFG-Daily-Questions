class Solution:
    def kokoEat(self, arr, k):
        left, right = 1, max(arr)
        answer = right
        
        while left <= right:
            mid = (left + right) // 2
            hours = 0

            for bananas in arr:
                hours += math.ceil(bananas / mid)

            if hours <= k:
                answer = mid
                right = mid - 1   
            else:
                left = mid + 1    

        return answer