def count(n):
    b = bin(n)
    a = []
    pos = 0
    while b.find('1', pos) != -1:
        a.append(b.find('1', pos))
        pos = b.find('1', pos) + 1
    max_zero = 0
    if len(a) == 1:
        return max_zero
    for i in range(len(a) - 1):
        if a[i + 1] - a[i] - 1 > max_zero:
            max_zero = a[i + 1] - a[i] - 1
    return max_zero





n = int(input())
print(count(n))
