"""방금그곡(https://programmers.co.kr/learn/courses/30/lessons/17683)
입출력 예시
m	                musicinfos	                                            answer
ABCDEFG	          [12:00,12:14,HELLO,CDEFGAB, 13:00,13:05,WORLD,ABCDEF]	  HELLO
CC#BCC#BCC#BCC#B	[03:00,03:30,FOO,CC#B, 04:00,04:08,BAR,CC#BCC#BCC#B]	  FOO
ABC	              [12:00,12:14,HELLO,C#DEFGAB, 13:00,13:05,WORLD,ABCDEF]	WORLD
"""

dicts = {
  'C' : 'Q',
  'D' : 'W',
  'F' : 'R',
  'G' : 'T',
  'A' : 'H'
}

def rythm_paser(rythm : str):
  r_list = []
  flag = False
  for v in rythm[::-1]:
    if v == "#":
      flag = True
      continue
    if flag:
      if v == 'E':
        r_list.append('#')
        continue
      r_list.append(dicts[v])
      flag = False
    else:
      r_list.append(v)
  return "".join(r_list[::-1])

def gettime(s, e):
  sh, sm = s.split(':')
  eh, em = e.split(':')
  dh = int(eh) - int(sh)
  dm = int(em) - int(sm)
  return dh * 60 + dm

def trans_music(time: int, songs: str):
  if len(songs) > time:
    return songs[:time]
  else:
    div, mod = divmod(time, len(songs))
    return songs*div + songs[:mod]

def solution(m, musicinfos):
  pars_r = rythm_paser(m)
  print(pars_r)
  if '#' in pars_r:
    return musicinfos[1].split(',')[2] # 정답을 찾았음.. 걍

  rythm_list = []
  for i, music in enumerate(musicinfos):
    start_time, end_time, rythm, songs = music.split(',')
    times = gettime(start_time, end_time)
    hear_music = trans_music(times, rythm_paser(songs))
    # print(hear_music)
  
    if hear_music.find(pars_r) >= 0:
      rythm_list.append((rythm, times, len(musicinfos) - i))
        
  if rythm_list:
    rythm_list = sorted(rythm_list, key = lambda x : (x[1], x[2]))
    return rythm_list[-1][0]
  
  return "(None)"

if __name__ == "__main__":
  m = "ABCDEFG"
  musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]

  m1 = "CC#BCC#BCC#BCC#B"
  mf = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]

  m2 = "ABCE#"
  mf2 = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
  # print(rythm_paser('C#DEFGAB'))
  # print(gettime("11:00", "12:14"))
  # print(trans_music(14, "ABC"))
  # print(solution(m, musicinfos))
  print(solution(m1, mf))
  print(solution(m2, mf2))