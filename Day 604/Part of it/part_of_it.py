class Solution:
    def isPart(self, n: int) -> str:
        n += 2
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return "No"
        return "Yes"