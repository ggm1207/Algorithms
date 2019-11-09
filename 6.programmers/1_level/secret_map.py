""" 비밀지도 (https://programmers.co.kr/learn/courses/30/lessons/17681)
매개변수	값
n	        5
arr1	    [9, 20, 28, 18, 11]
arr2	    [30, 1, 21, 17, 28]

출력	["#####","# # #", "### #", "# ##", "#####"]
"""



def solution(n, arr1, arr2):
  b_list = [2**v for v in range(n)][::-1]
  print(b_list)

  def n2b(n):
    b = []
    for v in b_list:
      if v <= n:
        b.append(1)
        n -= v
        continue
      b.append(0)
    return b
  
  arr_1_b = list(map(n2b, arr1))
  arr_2_b = list(map(n2b, arr2))
  arr_3 = [list(map(lambda x, y: x+y, v1,v2)) for v1, v2 in zip(arr_1_b, arr_2_b)]
  answer = []
  for ar in arr_3:
    s = ''
    for v in ar:
      if v > 0:
        s += '#'
      else:
        s += ' '
    answer.append(s)
  return answer


n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

if __name__ == "__main__":
  print(solution(n, arr1, arr2))
  