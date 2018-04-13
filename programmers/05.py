def sum_digit(number):
    result = 0
    for i in range(0, 1000):
        if number < pow(10, i):
            break;

    for j in range(i, 0, -1):
        result += number // pow(10, j - 1)
        number -= number // pow(10, j - 1) * pow(10, j - 1)

    return result

print(" result  : {}".format(sum_digit(123)));
# https://programmers.co.kr/learn/challenge_codes/116/solutions