class Solution:
    def getChocolateCost(self, arr, price):
        prev = 0
        balance = 0
        bought = 0
        for num in arr:
            balance +=(prev-num)
            if balance < 0:
                bought += abs(balance)
                balance = 0
            prev = num
        return bought*price