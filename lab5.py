

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = key

    return arr



data = [10, 5, 9, 2, 3, 7, 2, 6, 8, 1, 9, 7, 4]
print(insertion_sort(data)) 
