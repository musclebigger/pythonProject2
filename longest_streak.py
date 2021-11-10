# COMP1730 S2 2020 - final exam

# Implement the function longest_streak below.
# (The statement "pass" is just a placeholder that does nothing: you
# should replace it.)
# You can define other functions if it helps you decompose and solve
# the problem.
# Do NOT use global variables!
# Do NOT import any module that you do not use!

def longest_streak(seq):
    flag = 1 # This argument is a mark to find the number of the streak
    if 0 < len(seq) < 2:  # 2 elements and 0 element are a special case
        return 1
    if len(seq) == 0:
        return 0
    else:
        l = []
        for i in range(0, len(seq)-1):
            j = i+1
            if seq[i] > seq[j]:
                l.append(flag)
                flag = 1
            if seq[i] < seq[j]:
                flag = flag + 1
        l.append(flag)
        return( max(l) )


def test_longest_streak():
    '''
    This function runs a number of tests of the longest_streak function.
    If it works ok, you will just see the output ("all tests passed") at
    the end when you call this function; if some test fails, there will
    be an error message.
    '''

    assert longest_streak('acknowledgment') == 6
    assert type(longest_streak('acknowledgment')) == int
    assert longest_streak('tnemgdelwonkca') == 4
    assert longest_streak('biodegradability') == 4 
    assert longest_streak('ytilibadargedoib') == 2
    assert longest_streak('misunderstandings') == 5
    assert longest_streak('sgnidnatsrednusim') == 3
    assert longest_streak((0, 1, 2, 3, 4, 5, 6, 7, 8, 9)) == 10
    assert longest_streak((9, 8, 7, 6, 5, 4, 3, 2, 1, 0)) == 1
    assert longest_streak((0, 5, 1, 6, 2, 7, 3, 8, 4, 9)) == 2
    assert longest_streak((9, 4, 8, 3, 7, 2, 6, 1, 5, 0)) == 2

    print("all tests passed")

