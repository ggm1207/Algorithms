#include <iostream>
using namespace std;

#define MAX(a,b) (a) > (b) ? a : b
#define MIN(a,b) (a) < (b) ? a : b

int main(void)
{
  int n, min=1000001, max = -1000001;
  int g;
  cin>>n;
  for(int i=0; i<n; i++)
  {
    cin>>g;
    min = MIN(min,g);
    max = MAX(max,g);
  }
  cout<<min<<" "<<max<<endl;
  return 0;
} 