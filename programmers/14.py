def noOvertime(n, works):
    for i in range(n):
        pos = works.index(max(works))
        works[pos] -= 1
    for j in range(0, len(works)):
        works[j] = pow(works[j], 2)
    result = sum(works)
    return result

#https://programmers.co.kr/learn/challenge_codes/26