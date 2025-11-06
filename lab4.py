def comb_sort(arr):
    l = len(arr)
    step = l-1
    k = 1.247


    while(step>=1):
        for i in range(l-step):
               if arr[i]  > arr[i+step]:
                   arr[i], arr[i+step] = arr[i+step], arr[i]
        step = int(step/k)

    return arr


     
data = [ 9,4,3,5,6,2,1] 
print(comb_sort(data))
