def no _continuous(s):
    b=[]
    a = [i for i in str(s)]
    for i in range(len(s)):
        if a[i-1] is not a[i]:
            b.append(a[i])

    return b

#https://programmers.co.kr/learn/challenge_codes/86