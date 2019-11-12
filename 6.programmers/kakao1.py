


def solution(board, moves):
    N = len(board)
    stack = []
    stack_size = 0
    answer = 0
    
    board_rot90 = list(map(list,zip(*board[::-1])))
    board_rot90 = list(map(lambda x : list(filter(None, x)), board_rot90))

    for row in board_rot90:
        print(row)

    for mv in moves:
        if board_rot90[mv - 1]:
            v = board_rot90[mv - 1].pop()
            stack.append(v)
            stack_size += 1
        if stack_size > 1:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                stack_size -= 2
                answer += 2
    
    return answer


if __name__ == "__main__":
    board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    moves = [1,5,3,5,1,2,1,4]
    stack = []
    stack_size = 0
    answer = 0

    board_rot90 = list(map(list,zip(*board[::-1])))
    board_rot90 = list(map(lambda x : list(filter(None, x)), board_rot90))

    for row in board_rot90:
        print(row)

    for mv in moves:
        if board_rot90[mv - 1]:
            v = board_rot90[mv - 1].pop()
            stack.append(v)
            stack_size += 1
        if stack_size > 1:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                stack_size -= 2
                answer += 2

    for row in board_rot90:
        print(row)

    print(stack)
    print(answer)