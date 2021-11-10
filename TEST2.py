
def count_capitals(astring):
    """
    The argument must be a string.
    Returns the number of capital letters in the string.
    """
    pos = (len(astring) - 1)
    count = 0
    old_count = 0
    while pos >= 0:
        new_count = 0
        for a in ''.join([chr(x) for x in range(65, 65 + 26)]):
            if a in astring[pos:]:
                new_count = new_count + 1
        count = (new_count - old_count) + count
        old_count = new_count
        pos = pos - 1
    return count


print(count_capitals('AABBCDEF'))