class Solution:

    def findRank(self, str):
        fact = []
        fact.append(1)
        p = 1
        for i in range(2, 19):
            p *= i
            fact.append(p)

        l = len(str)
        mul = fact[l - 1]
        rank = 1

        count = [0] * 26

        for i in range(l):
            count[ord(str[i]) - 97] += 1

        for i in range(1, 26):
            count[i] += count[i - 1]

        for i in range(l):
            mul //= (l - i)

            x = ord(str[i]) - 98
            if x >= 0:
                rank += count[x] * mul

            for j in range(ord(str[i]) - 97, 26):
                count[j] -= 1

        return rank