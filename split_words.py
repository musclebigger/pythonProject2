# COMP1730 S2 2020 - final exam

# Implement the function split_words below.
# (The statement "pass" is just a placeholder that does nothing: you
# should replace it.)
# You can define other functions if it helps you decompose and solve
# the problem.
# Do NOT use global variables!
# Do NOT import any module that you do not use!

def split_words(astring):
    l = []
    flag = ''  # to identify letters
    word_list = [chr(x) for x in range(65, 65+26)] + [chr(y) for y in range(97, 97+26)]

    for i in range(0, len(astring)):
        if astring[i] in word_list:  # find the element which is not a letter
            if i != len(astring):
                flag = flag + astring[i]
            if i == len(astring)-1:  # supposed that the last value is a letter
                l.append(flag)
        elif len(flag) > 0:
            l.append(flag)
            flag = ''
    for e in l:
        if e == '':
            l.remove(e)
    return l


def test_split_words():
    '''
    This function runs a number of tests of the split_words function.
    If it works ok, you will just see the output ("all tests passed") at
    the end when you call this function; if some test fails, there will
    be an error message.
    '''

    assert split_words("This is a car, which I like.") == ["This", "is", "a", "car", "which", "I", "like"]
    assert split_words("/Users/foo/../bar/.") == ["Users", "foo", "bar"]
    assert split_words("Something - - else") == ["Something", "else"]

    assert split_words("") == []
    assert split_words("/,.{}") == []
    print("all tests passed")
