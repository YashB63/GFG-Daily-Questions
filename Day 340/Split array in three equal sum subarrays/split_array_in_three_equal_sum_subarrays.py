class Solution:
    
    def findSplit(self, arr):
        total_sum = sum(arr)
        if total_sum % 3 != 0:
            return [-1, -1]

        target_sum = total_sum // 3
        current_sum = 0
        first_index, second_index = -1, -1

        for i in range(len(arr)):
            current_sum += arr[i]

            if current_sum == target_sum and first_index == -1:
                first_index = i
            elif current_sum == 2 * target_sum and first_index != -1:
                second_index = i
                break

        if first_index != -1 and second_index != -1:
            last_part_sum = sum(arr[second_index + 1:])
            if last_part_sum == target_sum:
                return [first_index, second_index]

        return [-1, -1]