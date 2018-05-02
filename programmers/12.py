import math
def jumpCase(num):
        answer = 1
        for i in range(1,int(num/2)+1):
                answer += (increase(i,num-2*i))

        return answer


def increase(two,one):
        return math.factorial(two+one) / (math.factorial(two) * math.factorial(one))

print(jumpCase(10))
#https://programmers.co.kr/learn/challenge_codes/32 