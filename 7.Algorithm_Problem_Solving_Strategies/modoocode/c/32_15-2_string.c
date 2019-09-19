#include <stdio.h>

/* 
int main(){
    int num;
    char c;

    printf("input num:");
    scanf("%d", &num); # 1\n 입력값이 들어오고 num은 버퍼에서 1의 값만 가져간다.
    # 즉 버퍼에는 \n 이 남아 있는 상태
    printf("input str:");
    scanf("%c", &c); # %c 는 stdin에서 딴 한개의 문자만을 가져온다. \n 가져오게 되고 종료됨.

    return 0;
}
*/

/*
int main(){
    char str[30];
    int i;

    scanf("%d", &i);
    scanf("%s", &str); # 버퍼에 남아 있던 공백 문자들은 무시하고 실질적인 문자가 입력이 된다.

    printf("str : %s", str);

    return 0;
}
*/ 

/*
int main(){
    char str1[10], str2[10];

    printf("input str1 : ");
    scanf("%s", str1);
    printf("str1 : %s \n", str1);

    printf("input str2 : ");
    scanf("%s", str2);
    printf("str2 : %s \n", str2);

    return 0;
}
*/

/*
int main(){
    int num;
    char c;

    printf("input num : ");
    scanf("%d", &num);

    __fpurge(stdin); // buffer flush 해준다 # 생각해보니 예전에는 while문으로 버퍼 없앴던거 같은데..

    printf("input char : ");
    scanf("%c", &c);
    return 0;
}
*/

int main() {
  int num, i;
  char c;

  printf("숫자를 입력하세요 : ");
  scanf("%d", &num);

  while(getchar() != '\n');

  printf("문자를 입력하세요 : ");
  scanf("%c", &c);

  printf("입력한 문자 : %c", c);
  return 0;
}