def strange_sort(strings, n):
    for j in range(0,len(strings)-1):
        for i in range(j,len(strings)):
            if strings[j][n] >= strings[i][n] or (strings[j][n] == strings[i][n] and string[j][n+1] > strings[i][n+1]):
                a = strings[j]
                strings[j] = strings[i]
                strings[i] = a

    return strings

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( strange_sort(["sun", "bed", "car"], 1) )