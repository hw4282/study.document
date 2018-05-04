def nextBigNumber(n):
    count = 0
    sig = 0
    buf1 = 0
    answer = "0b"

    b = [i for i in bin(n)]
    b[1] = 0

    for buf in range(len(b) - 1, 1, -1):
        if b[buf - 1] == '0' and b[buf] == '1':
            break

        elif b[buf - 1] == '1' and b[buf] == '1':
            count += 1

        if b[buf] == '0':
            sig += 1


    b[buf - 1], b[buf] = 1, 0

    if count and sig >= 1:
        for a in range(1, sig + 1):
            b[buf + a], b[buf + count + a] = 0, 1

    for i in b :
        answer = str(answer) + str(i)

    return int(answer, 2)

print(nextBigNumber(78))
#https://programmers.co.kr/learn/challenge_codes/173