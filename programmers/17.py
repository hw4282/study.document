def hopscotch(board, size):
    for i in range(1, size):
        before_first_pos = board[i - 1].index(max(board[i - 1]))
        now_first_pos = board[i].index(max(board[i]))

        if before_first_pos == now_first_pos:
            buf = board[i - 1].copy()
            buf.sort()
            before_second_pos = board[i - 1].index(buf[-2])

            for j in range(4):
                if j == now_first_pos:
                    board[i][j] += board[i - 1][before_second_pos]
                    print("check")
                else:
                    board[i][j] += board[i - 1][before_first_pos]
        else:
            for j in range(4):
                board[i][j] += board[i - 1][before_first_pos]

    result = max(board[size - 1])
    return result


board = [[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]
print(hopscotch(board, 3))
#https://programmers.co.kr/learn/challenge_codes/35