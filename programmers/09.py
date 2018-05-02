def gcdlcm(a, b):
    test = []
    test.append(gcd(a, b))
    test.append(lcm(a, b))
    return test

def gcd(a, b):
    mod = a % b
    while mod != 0:
        a = b
        b = mod
        mod = a % b
    return b

def lcm(a, b):
    return a * b // gcd(a, b)

print(gcdlcm(3, 12))

# https://programmers.co.kr/learn/challenge_codes/11