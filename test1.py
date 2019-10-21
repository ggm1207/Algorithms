
section_list = [10]
num = 100

while(1):
    if num > 1000000000:
      break
    section_list.append(num - sum(section_list))
    num *= 10
    
real_list = section_list[:]
for i, v in enumerate(section_list):
  section_list[i] = v * (i+1)
    
def solution(n):
  # 1 <= n <= 1000000000
  # n 번째에 위치하는 수
  # section1 0 ~ 9 # 10
  # section2 10 ~ 99 # 90 * 2
  # section3 100 ~ 999 # 900 * 3
  
  tot_n = 0
  sec_num = 0
  for i, f_v in enumerate(section_list):
    tot_n += f_v
    if n < tot_n:
      sec_num = i + 1
      break

  # print('현재 속하는 섹션: ',sec_num)  
  tot_sec_num = section_list[sec_num - 1]
  cur_sec_num = n - sum(section_list[:sec_num-1]) # 현재 섹션에서 어디 위치
  which_num = (cur_sec_num % sec_num) # 자리수 거꾸로 나타냄 ex) 2섹션에서 0 이면 10의 자리 1이면 1의자리
  real_num = cur_sec_num // sec_num + sum(real_list[:sec_num-1])
  # print(real_num)
  answer = str(real_num)[which_num]
  # print('real:', real_num)
  # print(cur_sec_num)
  # print(section_list)
  # print(sum(section_list))
  # section = [10, ]
  return answer

print(solution(5))
print(solution(14))
print(solution(15))
print(solution(16))
print(solution(17))
print(solution(18))
print(solution(18))
print(solution(1003300))
print(solution(1020))
# p_cur = 0
# for i in range(1, 10000):
#   cur = i // 10 
#   if p_cur == cur:
#     end = ' '
#   else:
#     end = '\n'
#     p_cur = cur
#   print(solution(i), end = ' ')

