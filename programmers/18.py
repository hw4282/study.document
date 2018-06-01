def solution(n):
    half = (n // 2) + 1
    count = 0
    for i in range(1, half):
        result = 0

        for j in range(i, half + 1):
            result += j
            if result == n:
                count += 1
                break

            elif result >= n:
                break

    return count + 1

print(solution(15))
#https://programmers.co.kr/learn/courses/30/lessons/12924