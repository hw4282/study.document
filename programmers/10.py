def sumMatrix(a, b):
    buf_answer = []
    answer = []
    for i in range(len(a)):
        for j in range(len(a[0])):
            buf_answer.append(a[i][j] + b[i][j])
        answer.append(buf_answer)
        buf_answer = []

    return answer

    # https://programmers.co.kr/learn/challenge_codes/8