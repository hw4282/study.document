def caesar(s, n):
    buf = list(s)
    result = ""

    for i in range(0, len(buf)):
        if ord(buf[i]) == 32:
            result = result + str(buf[i])
            continue
        buf2 = ord(buf[i]) + n

        # if n > 27; i use while
        while (ord(buf[i]) < 91 and buf2 >= 91) or buf2 >= 123:
            buf2 -= 26

        buf[i] = chr(buf2)
        result = result + str(buf[i])

    return result
    #https://programmers.co.kr/learn/challenge_codes/23