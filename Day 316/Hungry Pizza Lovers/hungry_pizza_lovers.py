class Solution:
    def permute(self,arr,n):
        orders = []
        for i in range(n):
            order_time = arr[i][0]
            time_to_complete = arr[i][1]
            completion_time = order_time + time_to_complete
            orders.append((completion_time, i+1))
        orders.sort()
        result = [order[1] for order in orders]
        return result