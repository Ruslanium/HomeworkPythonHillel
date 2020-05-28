def rotation(a, n):
    for i in range(n):
        a.insert(0, a[-1])
        a.pop()
    return a


a = [3, 8, 9, 7, 6]
n = 3
print(rotation(a, n))
