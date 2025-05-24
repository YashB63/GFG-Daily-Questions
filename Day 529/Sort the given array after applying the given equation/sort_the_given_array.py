class Solution:
    def evaluate(self, x, A, B, C):
        return A * x * x + B * x + C

    def sortArray(self, arr, A, B, C):
        n = len(arr)
        newArr = [0] * n

        left, right = 0, n - 1
        index = n - 1 if A >= 0 else 0

        while left <= right:
            leftVal = self.evaluate(arr[left], A, B, C)
            rightVal = self.evaluate(arr[right], A, B, C)

            if A >= 0:
                if leftVal > rightVal:
                    newArr[index] = leftVal
                    left += 1
                    index -= 1
                else:
                    newArr[index] = rightVal
                    right -= 1
                    index -= 1
            else:
                if leftVal < rightVal:
                    newArr[index] = leftVal
                    left += 1
                    index += 1
                else:
                    newArr[index] = rightVal
                    right -= 1
                    index += 1

        return newArr