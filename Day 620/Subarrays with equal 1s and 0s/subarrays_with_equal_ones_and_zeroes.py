class Solution:
    def countSubarray(self, arr):
        um = defaultdict(int)
        curr_sum = 0

        for num in arr:
            curr_sum += -1 if num == 0 else num
            um[curr_sum] += 1

        count = 0
        for val in um.values():
            if val > 1:
                count += (val * (val - 1)) // 2

        if 0 in um:
            count += um[0]

        return count