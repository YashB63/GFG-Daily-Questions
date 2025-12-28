class Solution:
    def findMoves(self, chairs, passengers):
        chairs.sort()
        passengers.sort()
        ans = 0
        n = len(chairs)

        for i in range(n):
            ans += abs(chairs[i] - passengers[i])

        return ans