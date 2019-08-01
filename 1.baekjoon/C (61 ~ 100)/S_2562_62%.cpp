#include <iostream>
using namespace std;

int main(void)
{
  int num, max=0, j=0;
  for(int i=0; i<9; i++)
  {
    cin>>num;
    if (num > max)
    {
      j=i; max = num;
    }
  }
  cout<<max<<endl<<j+1<<endl;
  return 0;
}