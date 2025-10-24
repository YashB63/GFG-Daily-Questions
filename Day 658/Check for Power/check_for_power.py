class Solution:
    def isPowerOfAnother(ob, X, Y):
        if (X == 1):
            if (Y == 1):
                return 1
            else:
                return 0

        pow = 1
        while (pow < Y):
            pow = pow * X

        if (pow == Y):
            return 1
        else:
            return 0