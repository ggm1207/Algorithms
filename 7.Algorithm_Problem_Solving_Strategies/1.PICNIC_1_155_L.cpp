#include <iostream>
using namespace std;

// 문제 이름 : PICNIC
// c++ 로 처음 짜서 그런가.. 아니면 머리가 굳었나.. (핑계, 변명)
// 잘 모르겠어서 답지를 보았다...
// ps. stl 먼저 공부하는게 맞을 듯.. + c++ 감을 쉬운 문제를 풀면서 잡아야 겠다.

int n;
bool areFriends[10][10]; // false 로 초기화 되어 있음..

int countPairings(bool taken[10]){
  int firstFree = -1;
  for (int i=0; i<n; ++i){
    if(!taken[i]){
      firstFree = i;
      break;
    }
  }

  if(firstFree == -1) return 1;
  int ret = 0;

  for(int pairWith = firstFree+1; pairWith < n; ++pairWith){
    if(!taken[pairWith] && areFriends[firstFree][pairWith]){
      taken[firstFree] = taken[pairWith] = true;
      ret += countPairings(taken);
      taken[firstFree] = taken[pairWith] = false;
    }
  }
  return ret;
}

int main(void)
{
  int T; // 테스트케이스
  int m; // 친구쌍의 수
  cin>>T;
  for(int i=0; i<100; ++i){
    cin>>n>>m;
    for(int i=0;)

  }
  return 0;
}