## COMP1730/6730 S2 2020 - Homework 5
# Submission is due 9:00am, Monday the 5th of October, 2020.

## YOUR ANU ID: u6810586

## Implement the function interpolate below.
## (The statement "pass" is just a placeholder that does nothing: you
## should replace it.)
## You can define other functions if it helps you decompose the problem
## and write a better organised and/or more readable solution.

def interpolate(x, y, x_test):
    '''
    This function is to calculate the value of x_test based on linear interpolation.
    The function is based on that the length of sequence of x is same with the sequence of y.
    '''
    for n in range (len(x)):
        # If the sequence of elements in x align with a progressive increase
        if x[n] - x_test < 0 and x[n+1] - x_test >0:
            # the proportion is to calculate the slope of the linear which x_test belongs
            p = (x[n+1] - x_test)/(x_test - x[n])
            return int((y[n+1] + p*y[n])/(p + 1))
        # If the sequence of elements in x aligns with a progressive decrease
        if x[n] - x_test > 0 and x[n+1] - x_test <0:
            p = (x[n] - x_test) / (x_test - x[n+1])
            return int((y[n] + p * y[n+1])/(p + 1))
        # when x_test is in the x
        if x[n] - x_test == 0:
            return y[n]

def test_interpolate():
    '''
    This function runs a number of tests of the interpolate function.
    If it works ok, you will just see the output ("all tests passed") at
    the end when you call this function; if some test fails, there will
    be an error message.
    '''

    assert interpolate([1.0, 3.0, 5.0], [1.0, 9.0, 25.0], 2.0) == 5.0
    assert interpolate([1.0, 3.0, 5.0], [1.0, 9.0, 25.0], 4.0) == 17.0
    assert interpolate([1.0, 3.0, 5.0], [1.0, 9.0, 25.0], 1.25) == 2.0
    assert interpolate([1.0, 3.0, 5.0], [1.0, 9.0, 25.0], 2.5) == 7.0

    # test that we get the right answer when x_test is exactly one
    # of the sample points:
    assert interpolate([1.0, 3.0, 5.0], [1.0, 9.0, 25.0], 1) == 1.0
    assert interpolate([1.0, 3.0, 5.0], [1.0, 9.0, 25.0], 3) == 9.0
    assert interpolate([1.0, 3.0, 5.0], [1.0, 9.0, 25.0], 5) == 25.0

    # we should get the same answer also if only the two adjacent
    # sample points are given:
    assert interpolate([1.0, 3.0], [1.0, 9.0], 2.0) == 5.0
    assert interpolate([3.0, 5.0], [9.0, 25.0], 4.0) == 17.0

    print("all tests passed")


test_interpolate()