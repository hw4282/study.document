def string_middle(str):
    buf = len(str)
    value = int(buf / 2)
    if buf % 2 == 1:
        return str[value]
    elif buf % 2 == 0:
        return str[value - 1: value + 1]


print(string_middle("power"))
print(string_middle("Here"))

# https://programmers.co.kr/learn/challenge_codes/82
