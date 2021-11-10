
def selected_min(seq):
    x = 0
    while x < len(seq):
        if seq[x] == min(seq):
            return seq[x:]
        x = x+1

def max_increase(seq):
    seq1 = selected_min(list(seq))
    if len(seq) > 1:
        i = max(seq1) - min(seq1)
        return i
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
    assert max_increase([3, 2, 1, 1]) == 0.0, "no increasing pair";
    assert max_increase([226, 264, 337, 364, 485, 529, 482]) == 303.0
    btc_data = [6729.44, 6690.88, 6526.36, 6359.98, 6475.89, 6258.74,
                6485.10, 6396.64, 6579.00, 6313.51, 6270.20, 6195.01,
                6253.67, 6313.90, 6233.10, 6139.99, 6546.45, 6282.50,
                6718.22, 6941.20, 7030.01, 7017.61, 7414.08, 7533.92,
                7603.99, 7725.43, 8170.01, 8216.74, 8235.70, 8188.00,
                7939.00, 8174.06]
    btc_data.reverse()
    assert abs(max_increase(tuple(btc_data)) - 589.45) < 1e-6;
    print("all tests passed")

test_max_increase()