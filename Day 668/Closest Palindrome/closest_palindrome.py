class Solution:
    def closestPalindrome(self, num):
        if num < 10:
            return num

        d = []
        n = 0
        tn = num

        while tn:
            d.append(str(tn % 10))
            tn = tn // 10
            n += 1
        d = d[::-1]
        st = "".join(d)

        candidats = []
        candidats.append("9" * (n - 1))
        candidats.append("1" + "0" * (n - 1) + "1")
        prefix = int(st[:(n + 1) // 2])

        for pre in [prefix - 1, prefix, prefix + 1]:
            spre = str(pre)
            if n % 2 == 0:
                candidats.append(spre + spre[::-1])
            else:
                candidats.append(spre + spre[::-1][1:])

        return int(
            sorted(candidats, key=lambda x: (abs(num - int(x)), int(x)))[0])
