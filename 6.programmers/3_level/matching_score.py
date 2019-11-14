"""매칭 점수(https://programmers.co.kr/learn/courses/30/lessons/42893)
입출력 너무 길다.. pass
정규형을 소홀히한 내 잘못이지
"""
import re

class parser():
  def __init__(self, txt):
    self.txt = iter(txt)

  def readline(self):
    line = ''
    try:
      while(True):
        b = next(self.txt)
        if b == '\n':
          return line
        line += b
    except StopIteration:
      return line

def solution(word, pages):
  answer = 0
  return answer

if __name__ == "__main__":
  word = "blind"
  pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]

  body_parser = re.compile('<body>(.*)</body>', re.DOTALL)
  s, e = body_parser.search(pages[0]).span()
  real_body = pages[0][s+6:e-7].strip()
  print(pages[0][s+6:e-7].strip())

  base_score = re.compile(r'\b{}\b'.format(word), re.I)
  print(base_score.findall(real_body))

  