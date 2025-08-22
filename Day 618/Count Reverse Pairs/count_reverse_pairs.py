class Solution:
    def countRevPairs(self, arr):
        def sort_and_count(nums, l, r):
            if r - l <= 1:
                return 0
            m = (l + r) // 2
            cnt = sort_and_count(nums, l, m) + sort_and_count(nums, m, r)

            j = m
            for i in range(l, m):
                while j < r and nums[i] > 2 * nums[j]:
                    j += 1
                cnt += j - m

            temp = []
            i, j = l, m
            while i < m and j < r:
                if nums[i] <= nums[j]:
                    temp.append(nums[i]); i += 1
                else:
                    temp.append(nums[j]); j += 1
            while i < m:
                temp.append(nums[i]); i += 1
            while j < r:
                temp.append(nums[j]); j += 1

            nums[l:r] = temp
            return cnt

        return sort_and_count(arr, 0, len(arr))