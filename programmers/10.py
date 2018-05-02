def sumMatrix(a, b):
    buf_answer = []
    answer = []
    length = len(a)
    length1 = len(a[0])
    for i in range(length):
        for j in range(length1):
            buf_answer.append(a[i][j] + b[i][j])
        answer.append(buf_answer)
        buf_answer = []

    return answer

    # https://programmers.co.kr/learn/challenge_codes/8