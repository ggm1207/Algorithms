"""뉴스 클러스터링(https://programmers.co.kr/learn/courses/30/lessons/17677)
str1	    str2	  answer
FRANCE	  french	16384
handshake	shake   
          hands	  65536
aa1+aa2	  AAAA12	43690
E=M*C^2	  e=m*c^2	65536
"""
from string import ascii_lowercase

def solution(str1, str2):
  str1, str2 = str1.lower(), str2.lower()
  
  def only_ascii(v1,v2):
    if v1 in ascii_lowercase:
      if v2 in ascii_lowercase:
        return v1 + v2
    return None
  
  str1_2 = list(filter(None,[only_ascii(v1,v2) for v1, v2 in zip(str1[:-1], str1[1:])]))
  str2_2 = list(filter(None, [only_ascii(v1,v2) for v1, v2 in zip(str2[:-1], str2[1:])]))
  
  if str1_2 == str2_2 == []:
    return 65536

  intersection = union = 0
  for v in set(str1_2 + str2_2):
    intersection += min(str1_2.count(v), str2_2.count(v))
    union += max(str1_2.count(v), str2_2.count(v))
  
  answer = int(intersection / union * 65536)
  return answer

if __name__ == "__main__":
  str1 = 'handshake'
  str2 = 'shake hands'
  print(solution(str1, str2))