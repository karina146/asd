
def radix_sort(arr):
    
    max_digits = max([len(str(x)) for x in arr])

    base = 10
    bins = [[] for _ in range(base)]
   
    for i in range(0, max_digits):
        for x in arr:
            digit = (x // base ** i) % base
            bins[digit].append(x)
        arr = [x for j in bins for x in j]

        bins = [[] for _ in range(base)]
       
    return arr


data = []
print(radix_sort(data))
