def findKim(seoul):
    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
            a = i
            # 함수를 완성하세요
    return "김서방은 {}에 있다".format(a)

# 실행을 위한 테스트코드입니다.
print(findKim(["Queen", "Tod", "Kim"]))
#https://programmers.co.kr/learn/challenge_codes/105