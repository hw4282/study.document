def alpha_string46(s):
    try:
        a = int(s)
        if len(s) == 4 or len(s) == 6:
            return True

    except ValueError:
        return False


# 테스트 코드
print(alpha_string46("a234"))
print(alpha_string46("1234"))
print(alpha_string46("123456"))

# https://programmers.co.kr/learn/challenge_codes/99
