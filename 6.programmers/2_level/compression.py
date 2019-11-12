"""압축(https://programmers.co.kr/learn/courses/30/lessons/17684)
msg	                      answer
KAKAO	                    [11, 1, 27, 15]
TOBEORNOTTOBEORTOBEORNOT	[20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
ABABABABABABABAB	        [1, 2, 27, 29, 28, 31, 30]
"""
from string import ascii_uppercase

def solution(msg):
  msg_size = len(msg)
  dicts = {v: k+1 for k, v in enumerate(ascii_uppercase)}
  s_idx, e_idx = 0, 1
  key_idx = 27

  answer = []
  while(e_idx <= msg_size):
    cur_msg = msg[s_idx:e_idx+1]
    if cur_msg in dicts:
      if e_idx + 1 > msg_size:
        answer.append(dicts[cur_msg])
      e_idx += 1
      continue
    
    dicts[cur_msg] = key_idx
    key_idx += 1
    answer.append(dicts[msg[s_idx:e_idx]])
    s_idx = e_idx
    e_idx = s_idx + 1
    
  return answer

if __name__ == "__main__":
  dicts = {v: k+1 for k, v in enumerate(ascii_uppercase)}
  print(solution("KAKAO"))
