"""문자열 압축 (https://programmers.co.kr/learn/courses/30/lessons/60057)

제한사항
s의 길이는 1 이상 1,000 이하입니다.
s는 알파벳 소문자로만 이루어져 있습니다.

입출력 예
s	                        result
"aabbaccc"	                7
"ababcdcdababcdcd"	        9
"abcabcdede"	            8
"abcabcabcabcdededededede"	14
"xababcdcdababcdcd"	        17
"""

def cut_slice(s, n):
    string_list = []
    i = 0
    split = ""
    while(i < len(s)):
        if i % n == 0:
            string_list.append(split)
            split = ""
        split += s[i]
        i += 1
    string_list.append(split)
    return string_list[1:]

def solution(s):
    limit = len(s) // 2

    min_num = 10000

    if len(s) == 1:
        return 1

    for idx in range(1, limit + 1):
        string_list = cut_slice(s, idx)
        # print(string_list)
        new_str = ""
        cnt = 1
        cur_s = string_list[0]
        for ss in string_list[1:]:
            if cur_s == ss:
                cnt += 1
            else:
                if cnt == 1:
                    new_str += cur_s
                else:
                    new_str += str(cnt) + cur_s
                cur_s = ss
                cnt = 1
        if cnt == 1:
            new_str += cur_s
        else:
            new_str += str(cnt) + cur_s
        # print(new_str)
        min_num = min(len(new_str), min_num)     
    answer = min_num
    return answer

print(solution("a"))
print(solution("ab"))
print(solution("aabbaccc"))
print(solution("abcabcdede"))
print(solution("xababcdcdababcdcd"))