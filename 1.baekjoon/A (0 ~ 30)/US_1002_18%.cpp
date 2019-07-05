#include <iostream>
using namespace std;
typedef long long ll;
// 다시 돌아 온다....
#define DISTANCE(x1,y1,x2,r2) (((x1)-(x2))*((x1)-(x2))+((y1)-(y2))*((y1)-(y2)))
#define MAX(x,y) ((x) > (y)) ? x : y
#define MIN(x,y) ((x) < (y)) ? x : y

ll diffposition();
ll sameposition();

ll TestCase, x1, y1, r1, x2, y2, r2;

ll Turret()
{
  if(x1 == x2 && y1 == y2)
    return sameposition();
  else
    return diffposition();
}

ll sameposition() // 같은 좌표 일때
{
  if(r1 == r2) // 완전히 겹치는 원
    return -1;
  else // 서로 만나지 않는 두 원
    return 0;
}

ll diffposition() // 다른 좌표 일때
{
  ll btwr = (r1+r2)*(r1+r2); // (r1 + r2)^2
  ll btwxy = DISTANCE(x1,y1,x2,y2); // distance^2
  ll maxr = MAX(r1,r2)*MAX(r1,r2); // max r^2
  ll minr = MIN(r1,r2)*MIN(r1,r2); // min r^2

  if(btwr == btwxy) // r1 + r2 == distance 외접
    return 1;
  else if(btwr < btwxy) // r1 + r2 < distance 서로 만나지 않는 두 원
    return 0; 
  else // r1 + r2 > distance
  {
    if(btwxy < maxr) // 큰 원 안에 작은 원
    {
      if (btwxy + minr == maxr) // 내접
        return 1;
      else if(btwxy + minr > maxr)
        return 2;
      else // 내접 안함
        return 0;
    }
    else // 서로 두 개의 교차점을 가지며 만남
      return 2;
  }
}

int main(void)
{
  cin>>TestCase;
  for(ll TestNum=0; TestNum<TestCase; TestNum++)
  {
    cin>>x1>>y1>>r1>>x2>>y2>>r2;
    cout<<Turret()<<endl;
  }
  return 0;
}