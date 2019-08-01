#include <iostream>
using namespace std;
#define MAX(a,b) (a) > (b) ? a : b
int main(void)
{
  int max=0, total=0, num, n;
  cin>>n;
  for(int i=0; i<n; i++)
  {
    cin>>num;
    total += num;
    max = MAX(max,num);
  }
  cout<<(double)total/max*100/n<<endl;
}