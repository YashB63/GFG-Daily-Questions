class Solution:
    def getMin(self, x, y):
        return x if x < y else y

    def getAngle(self, s):
        h = int(s[:2])
        m = int(s[3:])

        h = h % 12

        hr_angle = 0.5 * (h * 60 + m)
        min_angle = 6 * m

        angle = abs(hr_angle - min_angle)

        return self.getMin(360 - angle, angle)