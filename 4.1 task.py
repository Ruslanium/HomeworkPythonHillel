def smallest_pos_int(a):
    a.sort()
    a = list(filter(lambda i: i > 0, a))
    if not a:
        return 1
    for i in range(len(a) - 1):
        if a[i + 1] - a[i] != 1:
            return a[i] + 1
    return a[-1] + 1


a = list(range(-1000000, 1000001))
print(smallest_pos_int(a))
