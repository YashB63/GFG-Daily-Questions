class Solution:
    def multiply_two_lists(self, first, second):
        num1=0
        while first:
            num1=(num1*10+first.data)%(10**9+7)
            first=first.next
        num2=0
        while second:
            num2=(num2*10+second.data)%(10**9+7)
            second=second.next
        return (num1*num2)%(10**9+7)