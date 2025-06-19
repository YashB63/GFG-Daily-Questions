class Solution:
    def maximumProfit(self, N, C, w, p):
        l = []
        
        for i in range(N):
            if w[i] != 0:
                l.append((p[i], w[i]))

        l.sort(key=lambda x: x[0] / x[1], reverse=True)
        prof = 0

        for i in l:
            if self.isperf(i[1]):
                continue
            else:
                if C - i[1] >= 0:
                    C -= i[1]
                    prof += i[0]
                    if C == 0:
                        return prof

                else:
                    fractn = C / i[1]
                    prof += i[0] * fractn
                    return prof

        return 9.9

    def isperf(self, num):
        if num**(0.5) == int(num**(0.5)):
            return True