def printTriangle(num):
    a = "*"
    b = "\n"
    c = ""
    for i in range(1, num + 1):
        c += (a * i) + b

    return c

print(printTriangle(3))
#https://programmers.co.kr/learn/challenge_codes/102