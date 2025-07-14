class Solution:
    def specialXor(self, N, Q, a, query):
        x = [0] * N
        ans = []

        x[0] = a[0]
        for i in range(1, N):
            x[i] = a[i] ^ x[i - 1]

        sep_xor = 0
        for q in query:
            l, r = q[0] - 1, q[1] - 1

            if l == 0:
                sep_xor = x[r]
            else:
                sep_xor = x[r] ^ x[l - 1]

            ans.append(x[N - 1] ^ sep_xor)

        return ans