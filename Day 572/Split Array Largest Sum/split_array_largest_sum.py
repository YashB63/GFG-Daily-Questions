class Solution:
    def check(self, mid, arr, k):
        n = len(arr)
        count = 0
        sum = 0
        for i in range(n):
            if (arr[i] > mid):
                return False

            sum += arr[i]

            if (sum > mid):
                count += 1
                sum = arr[i]
        count += 1

        if (count <= k):
            return True
        return False

    def splitArray(self, arr, k):
        n = len(arr)
        start = max(arr)
        end = sum(arr)

        answer = 0
        while (start <= end):
            mid = (start + end) // 2

            if (self.check(mid, arr, k)):
                answer = mid
                end = mid - 1
            else:
                start = mid + 1

        return answers