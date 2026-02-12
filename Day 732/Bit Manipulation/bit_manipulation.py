class Solution:
    def bitManipulation(self, num, i):
        mask = 1 << (i - 1)
        get_bit = (num >> (i - 1)) & 1
        set_bit = num | mask
        clear_bit = num & ~mask
        print(get_bit, set_bit, clear_bit)