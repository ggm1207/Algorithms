#include <iostream>
using namespace std;

int arr[1001] = {0,};
int ar[3] = {0,};

bool isHanSoo(int n)
{
  if (n < 100)
    return true;
  else if (n == 1000)
    return false;
  else
  {
    ar[0] = n/100;
    ar[1] = (n%100)/10;
    ar[2] = n%10;
    if (ar[1]*2 == ar[0] + ar[2])
      return true;
    else
      return false;
  }
}

int main(void)
{
  int num;
  for(int i=1; i<= 1000; ++i)
  {
    if(isHanSoo(i))
      arr[i] = arr[i-1] + 1;
    else
      arr[i] = arr[i-1];
  }
  cin>>num;
  cout<<arr[num]<<endl;
  return 0;
}
