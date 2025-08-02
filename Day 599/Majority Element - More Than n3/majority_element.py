class Solution:
    def findMajority(self, arr):
        n = len(arr)

        ele1, ele2 = -1, -1
        cnt1, cnt2 = 0, 0

        for ele in arr:
            if ele1 == ele:
                cnt1 += 1
            elif ele2 == ele:
                cnt2 += 1
            elif cnt1 == 0:
                ele1 = ele
                cnt1 += 1
            elif cnt2 == 0:
                ele2 = ele
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        res = []
        cnt1, cnt2 = 0, 0

        for ele in arr:
            if ele == ele1:
                cnt1 += 1
            if ele == ele2:
                cnt2 += 1

        if cnt1 > n // 3:
            res.append(ele1)
        if cnt2 > n // 3 and ele1 != ele2:
            res.append(ele2)

        if len(res) == 2 and res[0] > res[1]:
            res[0], res[1] = res[1], res[0]

        return res