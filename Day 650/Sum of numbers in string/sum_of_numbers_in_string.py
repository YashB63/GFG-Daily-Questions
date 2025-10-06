class Solution:
    def findSum(self, s):
        temp = "0"
        Sum = 0

        for ch in s:
            if (ch.isdigit()):
                temp += ch

            else:
                Sum += int(temp)
                temp = "0"

        return Sum + int(temp)
