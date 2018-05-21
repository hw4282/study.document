def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))
    return "".join(s)

print('s는 "a B z", n은 4인 경우: ' + caesar("a B z", 4))

return result
#https://programmers.co.kr/learn/challenge_codes/23