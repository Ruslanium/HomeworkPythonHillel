def multi(num):
    x = len(num)
    n = 0
    mul = 1
    while n < x:
        if num[n] == '0':
            n += 1
            continue
        else:
            mul *= int(num[n])
        n += 1
    return mul


num = str(input())
print(multi(num))