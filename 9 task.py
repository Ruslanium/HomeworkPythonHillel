def translate(n):
    list_rim = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
    list_num = list(range(1,11))
    if n.isalpha():
        for i in range(10):
            if n == list_rim[i]:
                return list_num[i]
    if n.isdigit():

        for i in range(10):
            if int(n) == list_num[i]:
                return list_rim[i]


n = input("Введите арабскую или римскую цифру(БОЛЬШИМИ БУКВАМИ): ")
print("Переведенная цифра:", translate(n))
