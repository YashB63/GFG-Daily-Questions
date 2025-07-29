class Solution:
    def minMeetingRooms(self, start, end):
        start.sort()
        end.sort()

        n = len(start)
        rooms = 0
        maxRooms = 0
        l = 0
        r = 0

        while l < n and r < n:
            if start[l] < end[r]:
                rooms += 1
                l += 1
            else:
                rooms -= 1
                r += 1

            maxRooms = max(maxRooms, rooms)

        return maxRooms