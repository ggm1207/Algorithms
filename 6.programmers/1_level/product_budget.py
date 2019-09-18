def solution(d, budget):
    d = sorted(d)
    tot = 0
    for i, v in enumerate(d):
        tot += v
        if tot > budget:
            i -= 1
            break
    answer = i + 1
    return answer

print(solution([1,3,2,4,5],9))
print(solution([2,2,3,3],10))