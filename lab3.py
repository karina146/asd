
def check(x):
    for p in [3, 5, 7]:
        while x % p == 0:
            x //= p
    return x == 1


def simple_multipliers(x):
    res = []
    for i in range(1, x + 1):
        if check(i):
            res.append(i)
    return res



x = int(input())
numbers = simple_multipliers(x)
print(*numbers)
