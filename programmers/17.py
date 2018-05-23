import copy


def hopscotch(board, size):
    result = 0
    for i in range(1, size):
        for j in range(4):
            temp = copy.deepcopy(board[i - 1])
            temp[j] = 0
            board[i][j] += max(temp)
    result = max(board[-1])
    return result

board = [[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]
print(hopscotch(board, 3))
#https://programmers.co.kr/learn/challenge_codes/35