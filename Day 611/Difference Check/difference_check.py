class Solution:
    def toSeconds(self, time: str) -> int:
        h = int(time[0:2])
        m = int(time[3:5])
        s = int(time[6:8])
        return h * 3600 + m * 60 + s

    def minDifference(self, arr: list[str]) -> int:
        total_sec = 24 * 3600

        seen = [False] * total_sec

        n = len(arr)

        for i in range(n):
            sec = self.toSeconds(arr[i])
            if seen[sec]:
                return 0
            seen[sec] = True

        first = -1
        last = -1
        prev = -1
        min_diff = float('inf')

        for i in range(total_sec):
            if not seen[i]:
                continue
            if prev != -1:
                min_diff = min(min_diff, i - prev)
            else:
                first = i
            prev = i
            last = i

        wrap = first + total_sec - last
        min_diff = min(min_diff, wrap)

        return min_diff