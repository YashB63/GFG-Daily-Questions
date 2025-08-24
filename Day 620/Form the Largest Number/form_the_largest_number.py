class Solution:
    def myCompare(self, s1, s2):
        if s1 + s2 > s2 + s1:
            return -1
        else:
            return 1

    def findLargest(self, arr):
        numbers = [str(ele) for ele in arr]

        numbers.sort(key=cmp_to_key(self.myCompare))

        if numbers[0] == "0":
            return "0"

        res = "".join(numbers)

        return res