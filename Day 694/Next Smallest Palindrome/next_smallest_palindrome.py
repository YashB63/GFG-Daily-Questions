class Solution:
    def generateNextPalindrome(self, num, n):
        def is_all_9s(num):
            return all(d == 9 for d in num)

        if is_all_9s(num):
            return [1] + [0] * (n - 1) + [1]

        result = num[:]
        mid = n // 2
        left = mid - 1
        right = mid if n % 2 == 0 else mid + 1

        while left >= 0:
            result[right] = result[left]
            left -= 1
            right += 1

        if result > num:
            return result

        carry = 1
        mid = n // 2
        if n % 2 == 1:
            result[mid] += carry
            carry = result[mid] // 10
            result[mid] %= 10
            left = mid - 1
            right = mid + 1
        else:
            left = mid - 1
            right = mid

        while left >= 0:
            result[left] += carry
            carry = result[left] // 10
            result[left] %= 10
            result[right] = result[left]
            left -= 1
            right += 1

        return result