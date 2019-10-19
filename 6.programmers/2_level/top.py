"""탑 (https://programmers.co.kr/learn/courses/30/lessons/42588)
입출력 예
heights	        return
[6,9,5,7,4]	    [0,0,2,2,4]
[3,9,9,3,5,7,2]	[0,0,0,3,3,3,6]
[1,5,3,6,7,6,5]	[0,0,2,0,0,5,6]
"""

def solution(heights):
    answer = []
    # [4 7 5 9 6]
    heights = heights[::-1]
    # print(heights)
    for idx, value in enumerate(heights):
        flag = True
        for mv_idx in range(idx + 1, len(heights)): # 1 2 3 4
            if value < heights[mv_idx]: # mv_idx 에서 수신됨
                answer.append(len(heights) - mv_idx)
                flag = False
                break
        if flag:
            answer.append(0)
    
    return answer[::-1]



print(solution([6,9,5,7,4]))
print(solution([3,9,9,3,5,7,2]))
print(solution([1,5,3,6,7,6,5]))