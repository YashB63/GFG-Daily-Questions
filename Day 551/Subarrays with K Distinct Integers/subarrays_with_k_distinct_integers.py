class Solution:
    def atMostK(self, arr, k):
        i = 0
        res = 0
        count = {}
        for j in range(len(arr)):
            if arr[j] not in count:
                count[arr[j]] = 0
                
            if count[arr[j]] == 0:
                k -= 1
            count[arr[j]] += 1

            while k < 0:
                count[arr[i]] -= 1
                if count[arr[i]] == 0:
                    k += 1
                i += 1

            res += j - i + 1
        return res

    def exactlyK(self, arr, k):
        return self.atMostK(arr, k) - self.atMostK(arr, k - 1)