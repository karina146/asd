

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2] 

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quicksort(left) + middle + quicksort(right)


data = [10, 5, 9, 2, 3, 7, 2, 6, 8, 1, 9, 7, 4]
print(quicksort(data))
