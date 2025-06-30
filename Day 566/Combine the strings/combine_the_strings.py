class Solution:
    def combine(self, n, s):
        a = [0] * 5
        sum2, max2, max3 = 0, 0, 0
        l = len(s[0])

        for i in range(n):
            if s[i][0] == 'R' and s[i][-1] == 'R':
                a[1] += 1
                max2 += 1
            elif s[i][0] == 'B' and s[i][-1] == 'B':
                a[2] += 1
                max3 += 1
            elif s[i][0] == 'B' and s[i][-1] == 'R':
                a[3] += 1
            elif s[i][0] == 'R' and s[i][-1] == 'B':
                a[4] += 1

        if a[3] == 0 and a[4] == 0:
            if a[1] == 1 and a[2] == 1:
                return 0
            else:
                max2 = l * max2
                max3 = l * max3
                return max(max2, max3)
        else:
            if a[3] > a[4]:
                sum2 += l * a[4]
                sum2 += l * (a[4] + 1)
                sum2 += l * a[1]
                sum2 += l * a[2]
                return 0 if sum2 == l else sum2
            elif a[4] > a[3]:
                sum2 += l * a[3]
                sum2 += l * (a[3] + 1)
                sum2 += l * a[1]
                sum2 += l * a[2]
                return 0 if sum2 == l else sum2
            else:
                sum2 += l * a[3]
                sum2 += l * a[3]
                sum2 += l * a[1]
                sum2 += l * a[2]
                return 0 if sum2 == l else sum2