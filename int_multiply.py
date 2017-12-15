import numpy as np
# Karastuba Multiplication


def karastuba(a, b):

    if len(a) == 1 == len(b):
        print('returning', a, b)
        return a[0] * b[0]

    n = len(max(a, b))
    n2 = int(n / 2)
    h1 = a[0:int(len(a)/2)]
    l1 = a[int(len(a)/2):len(a)]
    h2 = b[0:int(len(b)/2)]
    l2 = b[int(len(b)/2):len(b)]

    print(a, b, n, n2)
    print(h1, l1, h2, l2)
    print('z0')
    z0 = karastuba(l1, l2)
    print('z1')
    z1 = karastuba((l1+h1), (l2+h2))
    print('z2')
    z2 = karastuba(h1, h2)

    return (z2 * 10**(2 * n2)) + ((z1 - z2 - z0) * 10**n2) + z0


if __name__ == '__main__':
    # a = [int(x) for x in '3141592653589793238462643383279502884197169399375105820974944592']
    # b = [int(x) for x in '2718281828459045235360287471352662497757247093699959574966967627']

    a = [int(x) for x in '1000']
    b = [int(x) for x in '5000']
    c = ''.join(map(str, a))

    print(karastuba(a, b))
