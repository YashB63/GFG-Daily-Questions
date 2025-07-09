class Solution:
    def sort(self, arr, n):
        buckets = [[] for _ in range(n)]
        
        for num in arr:
            block = num // n
            buckets[block].append(num)
        
        result = []
        for bucket in buckets:
            bucket.sort()
            result.extend(bucket)

        for i in range(n):
            arr[i] = result[i]