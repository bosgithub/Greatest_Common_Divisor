''' Greatest common denominator

    this is used to find the largest common denominator given two numbers
    a and b'''


def greatest_common_denominator(a, b):
    # initialize the common denominator value: gcd
    gcd = []

    # check which number is the smaller one
    if a > b:
        smaller_one = b
    else:
        smaller_one = a

    # iterate from 1 to the smaller value to search for the biggest
    # common denominator
        for d in range(1, smaller_one + 1):
            # the iterator d has to be divisible by both a and b
            if (a % d == 0) and (b % d == 0):
                #
                gcd = gcd.append(d)
            else:
                return
    return gcd
