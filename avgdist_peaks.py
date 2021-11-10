# COMP1730 S2 2020 - final exam

# Implement the function avgdist_peaks below.
# (The statement "pass" is just a placeholder that does nothing: you
# should replace it.)
# You can define other functions if it helps you decompose and solve
# the problem.
# Do NOT use global variables!
# Do NOT import any module that you do not use!

def avgdist_peaks(seq):
    seq = list(seq)
    if len(seq) < 3:
        return 0.0
    if len(set(seq)) == 1:
        return 0.0
    else:
        peak_position = []
        for i in range(1, len(seq)):  # This iteration is to look for the position of peak value
            if seq[i] - seq[i - 1] < 0 and i == 1:  # This is the first value
                peak_position.append(i - 1)
            if seq[i] - seq[i - 1] > 0:
                if i == len(seq)-1:  # This is the last value
                    peak_position.append(i)
                else:
                    if seq[i + 1] - seq[i] < 0:
                        peak_position.append(i)
        if len(peak_position) < 2:
            return 0.0
        else:
            l = []
            t = 0  # calculate the combination of possible peak pairs
            while len(peak_position) > 0:  # This iteration is to compute the all situation of the distance of each pair peaks
                for x in range(0, len(peak_position)):
                    for i in range(0, len(peak_position) - 1):
                        m = peak_position[-1] - peak_position[i]  # All situation of last value has in terms of pair peaks
                        l.append(m)
                        t = t + 1
                    peak_position.pop(-1)
            return sum(l)/t


def test_avgdist_peaks():
    '''
    This function runs a number of tests of the avgdist_peaks function.
    If it works ok, you will just see the output ("all tests passed") at
    the end when you call this function; if some test fails, there will
    be an error message.
    '''

    assert abs(avgdist_peaks([13.0, 9.6, 14.2, 17.5, 8.9, 9.7, 15.7, 20.4, 14.8, 13.2, 13.6, 15.6, 17.9, 24.1, 19.2]) - 7.166666666666667) < 1e-6 

    assert abs(avgdist_peaks([2,4,6,8,4,6,8,6,8]) - 3.3333333333333335) < 1e-6
    assert type(avgdist_peaks([2,4,6,8,4,6,8,6,8])) == float

    assert abs(avgdist_peaks((1,0,1)) - 2.0) < 1e-6
    assert abs(avgdist_peaks((1,0))) < 1e-6
    assert abs(avgdist_peaks((0,1))) < 1e-6
    assert abs(avgdist_peaks((1,1,1))) < 1e-6
    
    assert type(avgdist_peaks((0,1))) == float
    assert type(avgdist_peaks((1,1,1))) == float

    assert abs(avgdist_peaks((0,1,0))) < 1e-6
    assert abs(avgdist_peaks((0,1,1,0))) < 1e-6

    print("all tests passed")

test_avgdist_peaks()