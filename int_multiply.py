from math import ceil, floor
# Karatsuba Multiplication


def karatsuba(x, y):

    if x < 10 and y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    n = int(ceil(float(n)/2))

    a = int(floor(x / 10**n))
    b = int(x % (10**n))

    c = int(floor(y / 10**n))
    d = int(y % (10**n))

    z1 = karatsuba(a, c)
    z2 = karatsuba(b, d)
    z3 = karatsuba(a + b, c + d) - z1 - z2

    return int(z1*(10**(n*2)) + z3*(10**n) + z2)


if __name__ == '__main__':
    x = 3141592653589793238462643383279502884197169399375105820974944592
    y = 2718281828459045235360287471352662497757247093699959574966967627

    #x = 1234
    #y = 56788

    result = karatsuba(x, y)
    print('=' * 25)
    print(result)
    print(x * y)
    if result == x * y:
        print('PASSED')
    else:
        print('FAILED')

