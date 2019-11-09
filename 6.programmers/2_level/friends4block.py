"""프렌즈4블록(https://programmers.co.kr/learn/courses/30/lessons/17679)
m	n	board	                                            answer
4	5	[CCBDE, AAADE, AAABF, CCBBF]	                    14
6	6	[TTTANT, RRFACC, RRRFCC, TRRRAA, TTMMMF, TMMTTJ]	15
"""

def solution(m, n, board):
  board = [list(s) for s in board]
  board = list(map(list,list(zip(*board[::-1]))))

  def isSame(v1,v2,v3,v4):
    if v1 == v2 == v3 == v4 == 0:
      return False
    return v1 == v2 == v3 == v4
  
  def get_idx():
    idx_list = []
    for y in range(n-1):
      for x in range(m-1):
        if isSame(
          board[y][x],
          board[y][x+1],
          board[y+1][x],
          board[y+1][x+1]
        ):
          idx_list.append((y,x))
    return idx_list

  def delete_board(idx_list, board):
    variable = [(0,0), (1,0), (0,1), (1,1)]
    delete_list = set()
    for y, x in idx_list:
      for a1, a2 in variable:
        board[y+a1][x+a2] = None
        delete_list.add((y+a1, x+a2))
    for i, row in enumerate(board):
      board[i] = list(filter(None, row))

    for i, row in enumerate(board):
      board[i] += [0 for i in range(n - len(row))]
    
    return board, len(delete_list)

  idx_list = get_idx()
  count = 0

  while(idx_list):
    board, vv = delete_board(idx_list, board)
    idx_list = get_idx()
    count += vv
  
  answer = count
  return answer

if __name__ == "__main__":
  m = 4
  n = 5
  board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
  print([list(s) for s in board])
  print(solution(m,n,board))