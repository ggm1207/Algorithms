"""기둥과 보 설치 (https://programmers.co.kr/learn/courses/30/lessons/60061)
입출력 예
n	build_frame	                                            result
5	[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],
    [5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]	            [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]
5	[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],
    [2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]	    [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]

"""

def solution(n, build_frame):
    answer = [[]]
    return answer