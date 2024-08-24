class Solution:
    def findOnce(self,arr : list, n : int):
        count_dict = {}
        for i in arr:
            if i in count_dict:
                count_dict[i] += 1
            else:
                count_dict[i] = 1

        for key,value in count_dict.items():
            if value==1:
                return key