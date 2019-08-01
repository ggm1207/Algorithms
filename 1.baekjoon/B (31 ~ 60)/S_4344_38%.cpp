#include <iostream>
using namespace std;

double avg()
{
  int num, cnt=0;
  double avg = 0;
  cin>>num;
  int arr[1000];
  for(int i=0; i<num; ++i)
  {
    cin>>arr[i];
    avg+=arr[i];
  }
  avg = avg/num;
  for(int i=0; i<num; ++i)
    if(arr[i] > avg)
      cnt++;
  return (double)cnt/num*100;
}

int main(void)
{
  int n;
  cin>>n;
  cout.precision(3);
  for(int i=0; i<n; ++i)
  {
    cout<<fixed<<avg()<<"%"<<endl;
  }
}