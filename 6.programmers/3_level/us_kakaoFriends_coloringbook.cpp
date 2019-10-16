/* 카카오 프렌즈 컬러링북 (https://programmers.co.kr/learn/courses/30/lessons/1829)
예제 입출력
m	n	picture	                                                                                answer
6	4	[[1, 1, 1, 0], [1, 2, 2, 0], [1, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 3], [0, 0, 0, 3]]	[4, 5]
*/

// 굉장히 쉬운 문젠데 아직 stl 에 익숙하지 않으므로 pass 왜 파이썬이 없냐..
#include <vector>

using namespace std;

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
vector<int> solution(int m, int n, vector<vector<int>> picture) {
    int number_of_area = 0;
    int max_size_of_one_area = 0;
    
    vector<int> answer(2);
    answer[0] = number_of_area;
    answer[1] = max_size_of_one_area;
    return answer;
}