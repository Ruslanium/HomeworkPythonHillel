def most_frequent(a):
    max_count = 0
    for i in a:
        if a.count(i) > max_count:
            max_count = a.count(i)
    res = []
    for i in a:
        if a.count(i) == max_count:
            res.append(i)
    return set(res)


a = ['a', 'a', 'bi', 'bi']
print(most_frequent(a))
