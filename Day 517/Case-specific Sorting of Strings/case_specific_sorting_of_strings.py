class Solution:
    def caseSort(self,s,n):
        upper = []
        lower = []

        for char in s:
            if char.isupper():
                upper.append(char)
            else:
                lower.append(char)

        upper.sort(reverse=True)
        lower.sort(reverse=True)

        sorted_string = ""

        for char in s:
            if char.isupper():
                sorted_string += upper.pop()
            else:
                sorted_string += lower.pop()

        return sorted_string