class Solution:
    def sum_of_middle_elements(self, arr1, arr2):
        merged_array = arr1+arr2
        sorted_array = sorted(merged_array)
       
        length_of_array = len(sorted_array)
        if length_of_array%2 !=0:
            return(sorted_array[int(length_of_array/2)])
        else:
            sum = sorted_array[int(length_of_array/2)]+sorted_array[int(length_of_array/2-1)]
            return sum