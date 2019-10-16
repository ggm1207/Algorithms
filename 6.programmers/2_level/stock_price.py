"""주식가격 (https://programmers.co.kr/learn/courses/30/lessons/42584?language=python3)
입출력 예
prices	
[1, 2, 3, 2, 3]
return
[4, 3, 1, 1, 0]
"""

# prices 원소를 하나 꺼내서
# 쭉 훑은다음에 값이 떨어지는 순간에 cut

def solution(prices):
    answer = [0 for _ in range(len(prices))]
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[j] < prices[i]:
                answer[i] = j - i
                break
            answer[i] = j - i
            
    return answer


prices =  [1, 2, 3, 2, 3]
print(solution(prices))