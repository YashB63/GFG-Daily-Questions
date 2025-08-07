class Solution:
    def powerfulInteger(self, intervals, k):
        mpp = {}

        for start, end in intervals:
            mpp[start] = mpp.get(start, 0) + 1
            mpp[end + 1] = mpp.get(end + 1, 0) - 1

        ans = -1
        temp = 0

        for point in sorted(mpp):
            delta = mpp[point]

            if delta >= 0:
                temp += delta
                if temp >= k:
                    ans = point
            else:
                if temp >= k:
                    ans = point - 1
                temp += delta

        return ans