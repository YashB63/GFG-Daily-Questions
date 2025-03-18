class Solution:
    def maxCoins(self, A, B, T, N):
        boxes = list(zip(A, B))

        boxes.sort(key=lambda x: x[1], reverse=True)

        total_gold = 0  
        for plates, coins in boxes:
            if T == 0:  
                break

            take_plates = min(plates, T)
            total_gold += take_plates * coins
            T -= take_plates  

        return total_gold