class Solution:
    def isHappy(self, num):
        seen = set()
        while num != 1 and num not in seen:
            seen.add(num)
            num = sum(int(d)**2 for d in str(num))
        return num == 1

    def nextHappy(self, N):
        N += 1
        while True:
            if self.isHappy(N):
                return N
            N += 1