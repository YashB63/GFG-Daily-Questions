class Solution:
    def startStation(self, gas, cost):
        n = len(gas)
        totalGas = 0
        currGas = 0
        startIdx = 0

        for i in range(n):
            currGas += gas[i] - cost[i]
            totalGas += gas[i] - cost[i]

            if currGas < 0:
                currGas = 0
                startIdx = i + 1

        if totalGas < 0:
            return -1

        return startIdx