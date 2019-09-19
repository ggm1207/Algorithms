def show_board(board, max_col, max_row):
    for row in range(max_row):
        for col in range(max_col):
            print("%2d" %board[row][col], end='')
        print()

def drop_block(board, col, row, max_row):
    """ col 번째 열 row 번째 행에서 부터 검은블록을 떨어트린다.
    """ 
    for r in range(row,max_row):
        # print(r, col, board[r][col])
        if board[r][col] == 0:
            board[r][col] = -1
            continue
        break

def inspect(row, col, max_row, max_col):
    return 0 <= row < max_row and 0 <= col < max_col

shapelist = [(1, -2), (2, -1), (2, 1), (1, 2)] # (add row,add col)
def is_shape(board, row, col, max_col, max_row):
    global shapelist
    isShape = False
    cur_val = board[row][col]
    # print(cur_val)
    if not isShape: # last ㅗ 
        cnt, b_cnt = 0, 0
        wegonext = False
        row1, row2, col1, col2 = row, row + 1, col - 1, col + 1
        if inspect(row1, col1, max_row, max_col) and inspect(row2, col2, max_row, max_col):
            # print(row1, row2, col1, col2)
            for r in range(row1, row2+1):
                for c in range(col1, col2+1):
                    # print(board[r][c] != cur_val, board[r][c] != -1)
                    if board[r][c] != cur_val and board[r][c] != -1 and board[r][c] != 0:
                        wegonext = True
                        break
                    if board[r][c] == cur_val:
                        cnt += 1
                    elif board[r][c] == -1:
                        b_cnt += 1
                if wegonext:
                    break
            isShape = True if cnt == 4 and b_cnt == 2 else False
            # print(isShape)
    else:
        pass

    for add_row, add_col in shapelist:
        if not isShape:
            cnt = 0
            b_cnt = 0
            wegonext = False
            row1, row2, col1, col2 = min(row, row + add_row), max(row, row + add_row), min(col, col + add_col), max(col, col + add_col)
            if inspect(row1, col1, max_row, max_col) and inspect(row2, col2, max_row, max_col):
                # print(row1, row2, col1, col2)
                for r in range(row1, row2+1):
                    for c in range(col1, col2+1):
                        # print(r, c, board[r][c])
                        # print(board[r][c] != cur_val, board[r][c] != -1)
                        if board[r][c] != cur_val and board[r][c] != -1 and board[r][c] != 0:
                            wegonext = True
                            break
                        if board[r][c] == cur_val:
                            cnt += 1
                        elif board[r][c] == -1:
                            b_cnt += 1
                    if wegonext:
                        break
                isShape = True if cnt == 4 and b_cnt == 2 else False
                # print(isShape)
                # print(cnt, b_cnt)
        else:
            break
    # print(cnt)
    if isShape:
        for r in range(row1, row2+1):
            for c in range(col1, col2+1):
                board[r][c] = 0

        for c in range(col1, col2+1):
            drop_block(board, c, row1, max_row)

    return 1 if isShape else 0


def solution(board):
    answer = 0
    max_col, max_row = len(board[0]), len(board)

    # 1. first blackblock drop
    for col in range(max_col):
        drop_block(board, col, 0, max_row)
    # show_board(board, max_col, max_row)
    # 2. find block
    for row in range(max_row):
        for col in range(max_col):
            if board[row][col] > 0:
                answer += is_shape(board, row, col, max_col, max_row)
            #    show_board(board, max_col, max_row)
            #    sleep(1)
    for row in range(max_row):
        for col in range(max_col):
            if board[row][col] > 0:
                answer += is_shape(board, row, col, max_col, max_row)
    # answer += is_shape(board,4,6,10,10)
    # print(answer)
    return answer