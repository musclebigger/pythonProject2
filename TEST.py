def split_words(astring):
    l = []
    flag = ''
    word_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    for i in range(0, len(astring)):
        if astring[i] in word_list:
            if i != len(astring):
                flag = flag + astring[i]
            if i == len(astring)-1:
                l.append(flag)
        elif len(flag) > 0:
            l.append(flag)
            flag = ''
    for e in l:
        if e == '':
            l.remove(e)
    return l



print(split_words("Something - - else"))

