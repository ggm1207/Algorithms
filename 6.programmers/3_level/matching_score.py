"""매칭 점수(https://programmers.co.kr/learn/courses/30/lessons/42893)
입출력 너무 길다.. pass
정규형을 소홀히한 내 잘못이지
"""
import re
from collections import defaultdict

## 80점 받음.. 시간 없으니 답지 보자 후..
def solution(word, pages):
  word, pages = word.lower(), [p.lower() for p in pages]
  word_score = [0]*len(pages)
  my_link, out_link = [""] * len(pages), [[] for _ in range(len(pages))]
  for idx, page in enumerate(pages):
    page = " " + re.sub(r'\n', '..', page) + " " # 깔끔하게 정리함으로써 풀기가 쉬워졌다.
    word_score[idx] = re.sub('[^a-z]+','.',page).split('.').count(word) # word를 이렇게 세셨군요..
    my_link[idx] = re.search(r'<meta.+?content="(https://.+?)"', page).group(1)
    out_link[idx] = re.findall('<a href="(https://.+?)">', page)
    
  total_score = [w for w in word_score]
  for i in range(len(pages)):
    for j in range(len(pages)):
      if my_link[i] in out_link[j]:
        total_score[i] += word_score[j] / len(out_link[j])
  return max(enumerate(total_score), key=lambda pair: (pair[1], -pair[0]))[0] # 뭐지 이 코드는
      

def prev_solution(word, pages):
  word = word.lower()
  bs_list = dict()
  mu_list = []
  matching_score = []
  link2index = defaultdict(list)
  linknum = defaultdict(int)

  body_parser = re.compile(r'<body>(.*?)</body>', re.DOTALL)
  url_parser = re.compile(r'<a href="(.*?)">.*?</a>')
  myurl_parser = re.compile(r'content="(.*?)"/>')
  base_score = re.compile(r'[^a-z]{}[^a-z]'.format(word))

  for idx, page in enumerate(pages):
    my_url = myurl_parser.search(page).group(1)
    real_body = body_parser.search(page).group(1).replace('\n', '\t').lower()
    
    url_in_body = url_parser.findall(real_body)
    bs = len(base_score.findall(real_body))
    
    bs_list[my_url] = bs
    mu_list.append(my_url)
    linknum[my_url] = len(url_in_body)
    for n_url in url_in_body:
      link2index[n_url].append(my_url)

  for idx, mu in enumerate(mu_list):
    bs_score = bs_list[mu]
    link_score = sum(list(map(lambda an: bs_list[an] / linknum[an] if linknum[an] != 0 else 0, link2index[mu])))
    matching_score.append(bs_score + link_score)

  return int(matching_score.index(max(matching_score)))

if __name__ == "__main__":
  word = "Muzi".lower()
  word = "blind"
  pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  \
    <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, \
      consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a> \n</body>\n</html>",\
         "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  \
           <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis \
             tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, \
               quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", \
                 "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n \
                    <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales \
                      rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n\
                        <a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
  # pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
  # print(pages[0])
  # print(pages[1])

  bs_list = dict()
  mu_list = []
  matching_score = []
  link2index = defaultdict(list)
  linknum = defaultdict(int)

  body_parser = re.compile(r'<body>(.*?)</body>', re.DOTALL)
  url_parser = re.compile(r'<a href="(.*?)">.*?</a>')
  myurl_parser = re.compile(r'content="(.*?)"/>')
  base_score = re.compile(r'[^a-z]{}[^a-z]'.format(word))

  # base_score = re.compile(r'(?!^{}|){}(?!^{})'.format(word[-1],word,word[0]), re.I)

  print(base_score)

  for idx, page in enumerate(pages):
    my_url = myurl_parser.search(page).group(1)
    real_body = body_parser.search(page).group(1).replace('\n', '\t').lower()
    # print(real_body)
    # print()
    url_in_body = url_parser.findall(real_body)
    print('url:', url_parser.findall(real_body))
    print('bs:', base_score.findall(real_body))
    bs = len(base_score.findall(real_body))
    
    bs_list[my_url] = bs
    mu_list.append(my_url)
    linknum[my_url] = len(url_in_body)
    for n_url in url_in_body:
      link2index[n_url].append(my_url)

  # print(bs_list)
  # print(mu_list)
  # print(link2index)
  for idx, mu in enumerate(mu_list):
    bs_score = bs_list[mu]
    link_score = sum(list(map(lambda an: bs_list[an] / linknum[an] if linknum[an] != 0 else 0, link2index[mu])))
    matching_score.append(bs_score + link_score)
  print(matching_score)
    