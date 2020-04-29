def degrees(arr, n):
    if len(arr) < n:
        return -1
    else:
        return arr[n] ** n


arr = [0, 2, 3, 4, 5]
n = int(input())
print(degrees(arr, n))