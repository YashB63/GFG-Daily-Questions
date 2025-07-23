class Solution:
    def countNumbers(self, n):
        c = 0
        limit = int(math.sqrt(n))

        prime = [i for i in range(limit + 1)]

        for i in range(2, int(math.sqrt(limit)) + 1):
            if prime[i] == i:
                for j in range(i * i, limit + 1, i):
                    if prime[j] == j:
                        prime[j] = i

        for i in range(2, limit + 1):
            p = prime[i]
            q = prime[i // prime[i]]

            if p * q == i and q != 1 and p != q:
                c += 1
                
            elif prime[i] == i and pow(i, 8) <= n:
                c += 1

        return c