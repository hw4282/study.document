def nlcm(a):
    length = len(a) - 1
    for i in range(0, length):
        a[i + 1] = a[i] * a[i + 1] // gcd(a[i], a[i + 1])
    return a[length]


def gcd(b, c):
    mod = b % c
    while mod != 0:
        b = c
        c = mod
        mod = b % c
    return c

#https://programmers.co.kr/learn/challenge_codes/29