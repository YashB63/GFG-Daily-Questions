class Solution:
    def totalFine(self, date, car, fine):
        n = len(car)
        even = 0
        odd = 0

        for i in range(n):
            if car[i] % 2 == 0:
                even += fine[i]
            else:
                odd += fine[i]

        if date % 2 == 0:
            return odd
        else:
            return even