def nonNegativeAverage(arr):
    result = [x for x in arr if x >= 0]
    avg = sum(result)/len(result)
    return avg