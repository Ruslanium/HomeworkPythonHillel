def find_word(mystr):
    list_str = list(mystr.split())
    count = 0
    for word in list_str:
        if word.isalpha():
            count += 1
            if count == 3:
                return True
        else:
            count = 0
    return False


mystr = "hello 1 one two three 15 world"
print(find_word(mystr))
