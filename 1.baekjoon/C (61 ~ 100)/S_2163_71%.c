#include <stdio.h>
#include <math.h>
int main()
{
    int a, b;
    int cho;
    scanf("%d %d", &a, &b);
    cho = a * (b - 1) + (a - 1);

    printf("%d", cho);
    return 0;
}