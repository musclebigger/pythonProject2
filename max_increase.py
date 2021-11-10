# COMP1730/6730 S2 2020 - Homework 4
# Submission is due 9:00am, Monday the 21st of September, 2020.

# YOUR ANU ID: u6810586
# YOUR NAME: Wancheng Fu

# Implement the function max_increase below.
# (The statement "pass" is just a placeholder that does nothing: you
# should replace it.)
# You can define other functions if it helps you decompose the problem
# and write a better organised and/or more readable solution.

def selected_min(seq):
    '''
    This function is to find the lowest point in the parameter
    and generate a new list which starts from the lowest point
    '''

    i = 0
    list = []
    while i < len(seq) - 1:
        different_value = seq[-1] - seq[i]
        list.append(different_value)
        i = i + 1
    return list

def max_increase(seq):
    '''
    This function is to calculate the increment between lowest point
    and highest point, which is based on that the lowest point is
    before the highest point.
    '''
    seq1 = list(seq)
    if len(seq1) > 1:
        list1 = []
        i1 = 1
        while i1 < len(seq1) - 1:
            list1 = list1 + selected_min(seq1)
            seq1 = seq1.pop(-i1)
        return max(list1)
    else:
        return 0

def test_max_increase():
    '''
    This function runs a number of tests of the max_increase function.
    If it works ok, you will just see the output ("all tests passed") at
    the end when you call this function; if some test fails, there will
    be an error message.
    '''

    assert max_increase([]) == 0.0, "empty list has no pair";
    assert max_increase([1]) == 0.0, "size-1 list has no pair";
    assert max_increase((1,2,3,2)) == 2.0;
    assert max_increase([1.0,3.0,1.0,2.0]) == 2.0;
    assert max_increase([3,-1,2,1]) == 3.0;
    assert max_increase([3,2,1,1]) == 0.0, "no increasing pair";
    assert max_increase([226, 264, 337, 364, 485, 529, 482]) == 303.0;

    btc_data = [ 6729.44, 6690.88, 6526.36, 6359.98, 6475.89, 6258.74,
                 6485.10, 6396.64, 6579.00, 6313.51, 6270.20, 6195.01,
                 6253.67, 6313.90, 6233.10, 6139.99, 6546.45, 6282.50,
                 6718.22, 6941.20, 7030.01, 7017.61, 7414.08, 7533.92,
                 7603.99, 7725.43, 8170.01, 8216.74, 8235.70, 8188.00,
                 7939.00, 8174.06 ]
    btc_data.reverse()
    assert abs(max_increase(tuple(btc_data))-589.45) < 1e-6;

    print("all tests passed")

selected_min([3,-1,2,1])