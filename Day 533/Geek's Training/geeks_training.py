class Solution:
    def maximumPoints(self, arr):
        n = len(arr)

        running, fighting, learning = arr[0]

        for i in range(1, n):
            tempRunning = arr[i][0] + max(fighting, learning)
            tempFighting = arr[i][1] + max(learning, running)
            tempLearning = arr[i][2] + max(fighting, running)

            running, fighting, learning = tempRunning, tempFighting, tempLearning

        return max(running, fighting, learning)