class Solution:
    def countPairs(self, arr):
        two_count = 0
        two_gr_count = 0

        for num in arr:
            if num == 2:
                two_count += 1
            elif num > 2:
                two_gr_count += 1

        return two_count * two_gr_count + (two_gr_count * (two_gr_count - 1)) // 2