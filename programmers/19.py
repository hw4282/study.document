def solution(n, s):
        a = 0
        answer =[]
        for i in range(1, n + 1):
                a += i
                if a > s:
                        return [-1]

        store = solution2(n, s, 0)
        for j in store:
                mux = 1
                for aa in j:
                        mux = mux * aa
                answer.append(mux)

        pos = answer.index(max(answer))
        return store[pos]


def solution2(n, s, h):
        if n == 2:
                half = s // 2
                v_list = []
                if s % 2 == 0:
                        balance = 1
                else:
                        balance = 0

                for i in range(half - balance):
                        if half - balance - i <= h:
                                break
                        else:
                                v_list.append([half - balance - i, half + i + 1])
                
                if v_list == [] or v_list is None:
                        return
                else:
                        return v_list
        else:
                former_v_list = []
                for i in range(h + 1, s // n):
                        buf = solution2(n - 1, s - i, i)
                        if buf is None or i + 1 >= s // 2:
                                break
                        else:
                                for j in range(len(buf)):
                                        buf[j].append(i)
                                        buf[j].sort()
                                        former_v_list.append(buf[j])
                
                return former_v_list

print(solution(4,15))
#https://programmers.co.kr/learn/courses/30/lessons/12938?language=python3