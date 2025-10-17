class Solution:
    def backtrack(self, arr, visited, curr, result):
        if len(curr) == len(arr):
            result.append(curr[:])
            return

        for i in range(len(arr)):
            if visited[i] or (i > 0 and arr[i] == arr[i - 1]
                              and not visited[i - 1]):
                continue

            visited[i] = True
            curr.append(arr[i])

            self.backtrack(arr, visited, curr, result)

            curr.pop()
            visited[i] = False

    def uniquePerms(self, arr):
        arr.sort()
        result = []
        visited = [False] * len(arr)

        self.backtrack(arr, visited, [], result)

        return result