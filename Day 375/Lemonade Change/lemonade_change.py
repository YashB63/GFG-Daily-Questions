class Solution:
    def lemonadeChange(self, N, bills):
        fives, tens = 0, 0
        for b in bills:
            if b == 5:
                fives += 1
            elif b == 10:
                fives -= 1
                tens += 1
            else: 
                if tens > 0:
                    tens -= 1
                    fives -= 1
                else:
                    fives -= 3
            if fives < 0:
                return False
        return True