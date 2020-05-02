def find_1_word(mystr):
    #mystr = mystr.strip()
    zn = '.,;:"'
    for i in range(len(zn)):
        mystr = mystr.replace(zn[i], '')
    list_str = mystr.split()
    for i in list_str:
        if len(i) > 1:
            return i


mystr = "   a  pull,.:;app'le aa,.:;"
print(find_1_word(mystr))
