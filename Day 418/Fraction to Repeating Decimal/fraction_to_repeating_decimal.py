class Solution:
    def calculateFraction(self, a, b):
        remainders = []
        before_decimal = str(a // b)
        after_decimal = ""
        remainder = a % b
        while remainder:
            if remainder in remainders:
                index_value = remainders.index(remainder)
                after_decimal = after_decimal[:index_value] + "(" + after_decimal[index_value:] + ")"
                return before_decimal + "." + after_decimal
            remainders.append(remainder)
            a = remainder * 10
            decimal_value = a // b
            after_decimal += str(decimal_value)
            remainder = a % b
            
        if after_decimal:
            return before_decimal + "." + after_decimal
        else:
            return before_decimal